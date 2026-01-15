# composer/music_generator.py
import os
import uuid
import torch
import numpy as np
from scipy.io.wavfile import write as wavwrite
from django.conf import settings
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# optional mp3 conversion via pydub (requires ffmpeg on PATH)
_MP3_OK = False
try:
    from pydub import AudioSegment
    _MP3_OK = True
except Exception:
    _MP3_OK = False

DEVICE = (
    "cuda" if torch.cuda.is_available()
    else "mps" if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()
    else "cpu"
)

def _media_abs(rel_path_noext: str) -> str:
    base = getattr(settings, "MEDIA_ROOT", os.path.join(os.getcwd(), "media"))
    abs_base = os.path.join(base, rel_path_noext)
    os.makedirs(os.path.dirname(abs_base), exist_ok=True)
    return abs_base

class MusicGenGenerator:
    def __init__(self, repo_id: str = "facebook/musicgen-small", sample_rate: int = 16000):
        self.repo_id = repo_id
        self.sample_rate = sample_rate
        self.model = None
        self.processor = None

    def _lazy_load(self):
        if self.model is None or self.processor is None:
            self.processor = AutoProcessor.from_pretrained(self.repo_id)
            self.model = MusicgenForConditionalGeneration.from_pretrained(self.repo_id)
            self.model.to(DEVICE)
            self.model.eval()

    def _norm_audio(self, audio: np.ndarray) -> np.ndarray:
        audio = np.asarray(audio, dtype=np.float32)
        if audio.ndim == 2:
            audio = audio.mean(axis=0)
        audio = np.clip(audio, -1.0, 1.0)
        return audio

    def _enforce_duration(self, audio: np.ndarray, duration_s: int) -> np.ndarray:
        desired_samples = int(duration_s * self.sample_rate)
        current = audio.shape[-1]
        if current > desired_samples:
            audio = audio[:desired_samples]
        elif current < desired_samples:
            pad = np.zeros(desired_samples - current, dtype=np.float32)
            audio = np.concatenate([audio, pad], axis=0)
        return audio

    def _save_audio_file(self, audio: np.ndarray, rel_base: str) -> str:
        abs_base = _media_abs(rel_base)
        wav_abs = abs_base + ".wav"
        wavwrite(wav_abs, self.sample_rate, (audio * 32767).astype(np.int16))

        if _MP3_OK:
            try:
                seg = AudioSegment.from_wav(wav_abs)
                mp3_abs = abs_base + ".mp3"
                seg.export(mp3_abs, format="mp3", bitrate="192k")
                try:
                    os.remove(wav_abs)
                except Exception:
                    pass
                return rel_base + ".mp3"
            except Exception:
                return rel_base + ".wav"
        return rel_base + ".wav"

    def generate_audio(self, prompt: str, duration_s: int = 12, guidance_scale: float = 3.0, style: str = "Track") -> str:
        self._lazy_load()
        inputs = self.processor(text=[prompt], padding=True, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            audio_values = self.model.generate(
                **inputs,
                do_sample=True,
                guidance_scale=guidance_scale,
                max_new_tokens=int(duration_s * 50),
            )
        audio = audio_values[0, 0].detach().cpu().numpy()
        audio = self._norm_audio(audio)
        audio = self._enforce_duration(audio, int(duration_s))
        rel_base = os.path.join("compositions", f"{style}_{uuid.uuid4().hex[:8]}")
        return self._save_audio_file(audio, rel_base)

# single shared instance
_musicgen = MusicGenGenerator()

def generate_music_file(style: str, prompt: str | None, duration_s: int) -> str:
    base_prompt = f"{style.lower()} instrumental track, coherent melody and harmony, high musicality"
    full_prompt = f"{base_prompt}. Details: {prompt.strip()}" if (prompt and prompt.strip()) else base_prompt
    try:
        return _musicgen.generate_audio(prompt=full_prompt, duration_s=int(duration_s), style=style)
    except Exception:
        # fallback silent file with exact duration
        desired = int(duration_s) * _musicgen.sample_rate
        rel_base = os.path.join("compositions", f"{style}_{uuid.uuid4().hex[:8]}")
        abs_path = _media_abs(rel_base) + ".wav"
        audio = np.zeros(desired, dtype=np.float32)
        wavwrite(abs_path, _musicgen.sample_rate, (audio * 32767).astype(np.int16))
        return rel_base + ".wav"
