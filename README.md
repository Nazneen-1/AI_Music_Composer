<div align="center">

  <a href="https://readme-typing-svg.demolab.com">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=32&pause=1000&color=8A2BE2&center=true&vcenter=true&width=600&height=70&lines=%F0%9F%8E%B5+AI+Music+Composer;Transform+Text+into+Melodies;Powered+by+PyTorch+%26+Django;Compose+the+Future+of+Sound" alt="AI Music Composer Typing SVG" />
  </a>

  <p align="center">
    <b>An intelligent, deep-learning powered web application that generates original music compositions from text prompts and musical styles.</b>
  </p>

  <p align="center">
    <a href="https://github.com/Nazneen-1/AI_Music_Composer/stargazers"><img src="https://img.shields.io/github/stars/Nazneen-1/AI_Music_Composer?style=for-the-badge&logo=github&color=7c3aed" alt="Stars"></a>
    <a href="https://github.com/Nazneen-1/AI_Music_Composer/network/members"><img src="https://img.shields.io/github/forks/Nazneen-1/AI_Music_Composer?style=for-the-badge&logo=github&color=9333ea" alt="Forks"></a>
    <a href="https://github.com/Nazneen-1/AI_Music_Composer/issues"><img src="https://img.shields.io/github/issues/Nazneen-1/AI_Music_Composer?style=for-the-badge&logo=github&color=c084fc" alt="Issues"></a>
    <a href="https://github.com/Nazneen-1/AI_Music_Composer/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Nazneen-1/AI_Music_Composer?style=for-the-badge&color=a855f7" alt="License"></a>
  </p>

</div>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,18,24,30&height=120&section=header&text=✨%20Key%20Features&fontSize=30&fontColor=ffffff&animation=twinkle" width="100%"/>
</div>

- 🎼 **AI Music Generation** &mdash; Convert text prompts and selected styles into unique audio compositions using state-of-the-art transformers.
- 🎨 **Style Selection** &mdash; Choose across diverse musical genres including Classical, Jazz, Lo-Fi, and Ambient.
- 💾 **Personal Music Library** &mdash; Save, manage, download, and favorite your generated tracks from your dashboard.
- ⚡ **Streamlined Architecture** &mdash; Django backend paired with PyTorch & HuggingFace inference pipeline.

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
| :--- | :--- |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) |
| **AI / Machine Learning** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) |
| **Audio Processing** | ![pydub](https://img.shields.io/badge/pydub-000000?style=for-the-badge&logo=audio&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white) ![music21](https://img.shields.io/badge/music21-4B0082?style=for-the-badge&logo=python&logoColor=white) |

</div>

---

## 📂 Project Structure

```ascii
ai_music_composer/
├── 🎵 composer/              # Main Django app (views, models, templates, music generator)
│   ├── static/             # Frontend assets & styles
│   ├── templates/          # HTML templates & user dashboards
│   ├── models.py           # Composition & user models
│   └── music_generator.py  # AI generation inference pipeline
├── ⚙️ music_project/         # Django project core configuration
├── 🧠 models/                # Local model weights directory (MusicGen / transformers)
├── 📄 manage.py              # Django management CLI
└── 📋 requirements.txt       # Project dependencies
```

---

## 🧠 Model Setup

> [!NOTE]
> Pre-trained AI model weights are excluded from Git due to file size limits.

Create a `models/` directory in the project root and download the target model weights (e.g., `facebook/musicgen-small`):

```bash
mkdir -p models/musicgen-small
```

---

## 🚀 Quick Start Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Nazneen-1/AI_Music_Composer.git
cd AI_Music_Composer
```

### 2️⃣ Virtual Environment Setup
```bash
# On Linux / macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Database Migration & Launch
```bash
python manage.py migrate
python manage.py runserver
```

🌐 Open your browser at **`http://127.0.0.1:8000/`** to start composing!

---

<div align="center">

### 👩‍💻 Author

**Nazneen Firdous**
[![GitHub](https://img.shields.io/badge/GitHub-Nazneen--1-181717?style=for-the-badge&logo=github)](https://github.com/Nazneen-1)

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,18,24,30&height=100&section=footer" width="100%"/>

</div>
