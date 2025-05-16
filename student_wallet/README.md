# Student Wallet - Budget Tracker

A simple Django web application to help students manage their budgets by tracking categories and transactions, with user authentication handled via a dedicated accounts app.

---

## Features

- User registration, login, and logout via the **accounts** app
- Add, edit, and delete budget categories
- Add, edit, and delete transactions
- View category spending and remaining budget
- Responsive and clean UI using Bootstrap and Crispy Forms

---

## Tech Stack

- Python 3.x
- Django 5.x
- Bootstrap 4/5
- Crispy Forms for elegant form rendering
- SQLite (default Django database, can be changed)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/student-wallet.git
   cd student-wallet

---

## Project structure

student_wallet/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── budget/
│   ├── migrations/
│   ├── templates/
│   │   └── budget/
│   ├── templatetags/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── student_wallet/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
