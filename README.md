# 💬 Chats App

A modern **real-time chat application** built with **Django** and **TailwindCSS**.  
Users can create chat rooms, register/login securely, and chat in an elegant, responsive UI.

---

## ✨ Features
- 🔐 User Authentication (Register, Login, Logout)
- 🏠 Create & Join Chat Rooms
- 💬 Real-time Messaging (with modern UI)
- 🎨 Beautiful design with TailwindCSS
- 📱 Fully responsive (desktop + mobile)

---

## 📸 Screenshots
*(Add some screenshots of your login, register, and chat room pages here!)*

---

🛠️ Tech Stack

Backend: Django

Frontend: TailwindCSS

Database: SQLite (default, easy to switch to PostgreSQL/MySQL)

Authentication: Django built-in auth system


## ⚙️ Installation

# 1. Clone the repository
git clone https://github.com/Soham-Kamble/Real-Time-Chat-Application
cd mysite

# 2. Create and activate a virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Create a .env file in the project root and add:
# SECRET_KEY=your-django-secret-key
# DEBUG=True

# 4. Apply database migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

