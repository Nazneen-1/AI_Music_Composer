<div align="center">
  <a href="https://github.com/Nazneen-1/Museon">
    <img src="https://readme-typing-svg.demolab.com?font=Outfit&weight=600&size=32&pause=1000&color=FF5E8C&center=true&vcenter=true&width=600&height=70&lines=%F0%9F%8E%B5+Museon;AI+Music+Composer;Turn+Your+Ideas+into+Music;Powered+by+Django+%26+PyTorch" alt="Museon Typing SVG" />
  </a>
</div>

# Museon

**AI Music Composer**

Museon is a Django-based web application that empowers users to generate AI-composed music and easily manage their generated compositions in a sleek, modern interface.

## ✨ Features

- **User Authentication:** Complete user registration, login, and logout flow.
- **Secure Sessions:** Standard Django session-based authentication.
- **AI Music Generation:** Generate unique audio tracks based on chosen styles, durations, and text prompts.
- **Composition Management:** View, organize, and manage generated audio files.
- **Audio Playback:** Built-in HTML5 audio player for immediate listening.
- **Favorites System:** Mark generated tracks as favorites for quick access.
- **Audio Downloads:** Download generated `.wav` files directly to your device.
- **Filtering:** Toggle between viewing all tracks and only favorited tracks.
- **Responsive UI:** Fully responsive, mobile-first glassmorphism design that works seamlessly across all devices.

## 🎯 Project Overview

Museon provides a creative workspace for generating original AI music. Whether for background tracks, inspiration, or just for fun, Museon removes the technical barrier to music creation. Users simply describe the sound they want or select a predefined style, and the underlying AI pipeline handles the rest, generating an audio file that can be played, saved, and downloaded directly from their dashboard.

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5, Three.js (3D Backgrounds) |
| **Backend** | Python 3, Django 5.2.5 |
| **Database** | SQLite3 |
| **Authentication** | Django Session Authentication |
| **AI / Music Generation** | PyTorch, Transformers, HuggingFace Hub, SciPy, PyDub, Music21 |
| **Static Files** | WhiteNoise |
| **Production Server** | Gunicorn |

## 🏗️ Architecture

The application relies on a straightforward, synchronous MVT (Model-View-Template) architecture:

```text
User 
  ↓ (HTTP Request)
Django Web Application (Routing & Views)
  ↓
Music Generation Pipeline (PyTorch/Transformers)
  ↓
Composition Database (SQLite)
  ↓
Generated Audio Files (Local Media Storage)
```

## 📁 Project Structure

```text
Museon/
├── composer/               # Main application module
│   ├── templates/          # HTML templates (landing, index, auth)
│   ├── static/             # Static assets (favicon, custom CSS)
│   ├── models.py           # Database models (Composition)
│   ├── views.py            # Application logic and routing
│   ├── urls.py             # App-level URL configurations
│   └── music_generator.py  # Local AI music generation logic
├── music_project/          # Django project configuration
│   ├── settings.py         # Core settings (Env vars, Middleware, WSGI)
│   ├── urls.py             # Root URL routing
│   └── wsgi.py             # WSGI entry point for Gunicorn
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
└── manage.py               # Django management script
```

## 🔐 Authentication

Museon uses robust, out-of-the-box **Django Session Authentication**. 
- The application securely handles standard `signup`, `login`, and `logout` views.
- The main application dashboard (`/app/`) and generation routes are protected.
- Unauthenticated users are redirected to the login page.
- *Note: This project uses session cookies, not JWT.*

## 🎵 Music Generation

Music generation is powered by a local, model-based AI pipeline implemented in `music_generator.py`. Using PyTorch, Transformers, and SciPy, the backend interprets user parameters (Style, Prompt, Duration) and synthesizes a unique audio file. The output is processed via PyDub and saved to disk before returning the path to the database model.

## 💾 Data & Storage

- **Database:** Currently utilizes a local **SQLite** (`db.sqlite3`) database. It stores the Django `User` models and the `Composition` records (which map users to their generated files).
- **Media Storage:** Generated `.wav` files are saved to the local `media/` directory on the server's filesystem.

*(See Production Notes regarding data persistence).*

## 🎨 User Interface

The UI is built with a premium, dynamic "glassmorphism" aesthetic using the Museon color palette. 
- **Landing Page:** Features a responsive 3D WebGL background powered by Three.js.
- **Dashboard:** A clean, stacked layout (mobile-first) that prevents horizontal scrolling. It elegantly wraps generation controls, play buttons, and composition metadata.

## ⚙️ Local Setup

Follow these steps to run Museon locally on Windows:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nazneen-1/Museon.git
   cd Museon
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   *(Edit `.env` to supply necessary development values).*

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Open the application:**
   Navigate to `http://127.0.0.1:8000` in your browser.

## 🔑 Environment Variables

The project uses the following environment variables (refer to `.env.example`):

- `SECRET_KEY`: Django's cryptographic key (Required for production).
- `DEBUG`: Set to `True` for local development; must be `False` in production.
- `ALLOWED_HOSTS`: Comma-separated list of valid domain names.
- `CSRF_TRUSTED_ORIGINS`: Comma-separated list of trusted origins for CSRF protection.

*Never expose actual secrets, API keys, or tokens in version control.*

## 🧪 Verification

You can run the following commands to verify the integrity of the application:

```bash
python manage.py check
python manage.py test
```

## 🚀 Production Notes

Museon is structurally prepared for a WSGI production deployment using **Gunicorn**. 
- Production-grade static file serving is implemented via **WhiteNoise**.
- Security settings (Secure Cookies, SSL Redirects, HSTS) automatically engage when `DEBUG=False`.

**⚠️ Deployment Blockers:** 
Museon currently relies on ephemeral local storage for the SQLite database and `media/` folder. A production deployment requires appropriate persistent database (e.g., PostgreSQL) and media storage infrastructure (e.g., Amazon S3) before going live on platforms like Heroku, Render, or Vercel.

## 🔮 Future Improvements

- Migrate to PostgreSQL for robust, concurrent data persistence.
- Integrate Amazon S3 (or similar object storage) via `django-storages` for generated audio files.
- Add additional generation styles and granular track-editing controls.

## 📄 License

This repository currently does not specify a license.

## 👩‍💻 Author

GitHub: [Nazneen](https://github.com/Nazneen-1)