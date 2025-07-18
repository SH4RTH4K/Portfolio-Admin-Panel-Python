# Portfolio Admin Panel (Python)

A customizable and easy-to-use admin panel built with Python for managing your personal or professional portfolio. This tool allows you to add, update, and display portfolio content through an admin interface—no coding required!

## 🚀 Features

- 🧑‍💼 Admin panel for easy content management
- 📝 Add/edit portfolio items (projects, skills, experience, etc.)
- 📁 Upload project images and files
- 📊 Dashboard overview
- 🔐 Authentication (Login system)
- 🌐 Ready for deployment on any server

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap)
- **Deployment**: GitHub

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SH4RTH4K/Portfolio-Admin-Panel-Python.git

2. Create a Virtual Environment

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Server

python manage.py migrate
python manage.py createsuperuser  # Create your admin account
python manage.py runserver

Now go to: http://127.0.0.1:8000/admin to log in and manage your portfolio.


portfolio_admin_panel_python/
│
├── portfolio/             # Main app
├── media/             # Image
├── static/                # Static assets (CSS/JS)
├── templates/             # HTML templates
├── db.sqlite3             # Default DB (can be changed)
├── manage.py              # Django entry point
└── README.md              # Project info

📄 License

This project is open-source and available under the MIT License.
🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.
