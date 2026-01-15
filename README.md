# 🎵 AI Music Composer

AI Music Composer is a Python and Django-based project that generates music using pre-trained deep learning models.  
This repository contains the application code only; large AI model files are intentionally excluded due to GitHub size limits.

---

## 🚀 Features

- AI-powered music generation
- Uses pre-trained music generation models
- Django backend
- Clean project structure
- Large files excluded using `.gitignore`

---

## 🛠️ Tech Stack

- Python
- Django
- PyTorch / Deep Learning Models
- SQLite
- Git & GitHub

---

## 📂 Project Structure

```
ai_music_composer/
├── composer/
├── music_project/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Model Setup

AI model files are not included in this repository.

Create a folder named `models/` in the project root and place the downloaded model files inside it.

```
models/
└── musicgen-small/
```
---

## ⚙️ Installation & Setup

### Clone the repository
```
git clone https://github.com/Nazneen-1/AI_Music_Composer.git
cd AI_Music_Composer
```

### Create and activate virtual environment
```
python -m venv Venv
Venv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Apply migrations
```
python manage.py migrate
```

### Run the server
```
python manage.py runserver
```
Open:
```
http://127.0.0.1:8000/
```

---

## 🔐 Environment Variables

Create a `.env` file if required.  
`.env` files are ignored by Git.

---

## 📌 Notes

- Models and media files are excluded from version control
- Repository contains code only
- Suitable for learning and experimentation

---

## 👩‍💻 Author

Nazneen Firdous  
GitHub: https://github.com/Nazneen-1
