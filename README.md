# 🚑 MedTrack Pro

**MedTrack Pro** is a hospital management system developed by **Pratyush Paradarshi Patra** using Django and MySQL. It helps hospitals go digital by managing appointments, patient records, and prescriptions in a paperless and efficient format.

![Made with Django](https://img.shields.io/badge/Framework-Django-green)
![Database](https://img.shields.io/badge/Database-MySQL-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

---

## 🧠 Features

- 👨‍⚕️ User Authentication: Patients, Doctors, Admins
- 📅 Appointment Booking & Management
- 📂 Upload & Access Medical Reports and Prescriptions
- 🧑‍⚕️ Doctor Dashboard with Patient Info
- 🛡️ Admin Dashboard to Manage Everything
- 💻 Responsive Frontend using Bootstrap 5

---

## ⚙️ Tech Stack

| Technology | Description              |
|------------|--------------------------|
| Django     | Backend framework (Python) |
| MySQL      | Relational Database       |
| HTML/CSS   | Frontend Layout           |
| Bootstrap  | Styling & Responsiveness  |
| Git & GitHub | Version Control          |

---

## 🚀 Installation Guide

### Step 1: Clone the Repo
```bash
git clone https://github.com/yourusername/medtrack_pro.git
cd medtrack_pro

##Create Virtual Environment
python -m venv venv
# Activate
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
##Install Requirements
pip install -r requirements.txt

Configure MySQL in medtrack_pro/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### Migrate & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser


### python manage.py runserver
Visit the app at: http://127.0.0.1:8000/


🧩 Folder Structure
medtrack_pro/
│
├── medtrack_pro/           # Django settings and urls
│   ├── settings.py
│   └── urls.py
├── app/                    # Django app logic
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
├── static/                 # CSS, JS files
├── templates/              # HTML templates
├── manage.py
├── requirements.txt
└── README.md

# 👨‍💻 Usage

**Patients**: Sign up, log in, book appointments, upload/view reports.  
**Doctors**: Manage appointments, view patient history and prescriptions.  
**Admins**: Access admin panel to manage users and system data.

---

# 🌐 Live Demo

**Coming soon...**  
*(Host it on Render / Railway / Heroku and add the link here)*

---

# 🤝 Contributing

**Pull requests are welcome.**  
If you have suggestions or bugs, open an issue or fork the project and create a PR.

---

# 📜 License

**This project is licensed under the MIT License.**  

