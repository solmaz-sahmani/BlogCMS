# 📝 Django Blog Project

A simple blog system built with Django and Docker, featuring:

- 🐳 Dockerized setup (easy to run anywhere)
- 🗄 Django ORM with SQLite (or PostgreSQL in production)
- 🔐 User authentication (register, login, logout)
- ✍️ Post creation (only for logged-in users)
- 📄 Admin panel for managing posts & categories
- 🎨 Simple HTML template with static CSS/JS support

---

## ⚙️ Tech Stack

- Python 3.10
- Django 4.x
- Gunicorn (for production-ready server)
- Docker & Docker Compose
- SQLite (development) / PostgreSQL (production)

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/solmaz-sahmani/Blog-CMS.git
cd Blog-CMS
```
---

### 2️⃣ Build and run with Docker

```bash
docker-compose up --build
```

Visit: http://localhost:8000

---

## 👨‍💻 Default Features

- Home page → list all posts
- Post detail → show full content and author info
- User auth → register/login/logout
- Create post → only logged-in users can create
- Admin panel → manage posts and categories

---

## 📂 Project Structure
```bash

blog_cms/
├── blog/           # Blog app (views, models, urls)
├── core/           # Main Django project settings
├── static/         # CSS, JS, images
├── templates/      # HTML templates
├── Dockerfile
├── compose.yml
└── manage.py
```
---

## 📊 Project Architecture

    Browser (User)
        │
        ▼
    Django + Gunicorn (Docker)
        │  ORM
        ▼
    SQLite / PostgreSQL
