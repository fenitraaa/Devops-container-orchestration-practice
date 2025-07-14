# 🚀 Flask MySQL CRUD App

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-orange)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)](https://www.mysql.com/)

---

## 📄 Project Overview

This is a simple **Flask + MySQL CRUD (Create, Read, Update, Delete) Web Application** built **for learning purposes only**.
It demonstrates basic CRUD operations on user records using **Flask** as the web framework and **MySQL** as the database.

It also includes additional demonstration pages for:

* Displaying the **current date and time**
* Performing a **simple addition of two numbers** via a form

---

## 🛠️ Tech Stack

| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| **Python 3.9+**     | Core Programming Language        |
| **Flask 2.3+**      | Web Framework                    |
| **MySQL 8.0+**      | Relational Database              |
| **MySQL Connector** | Python to MySQL Connection       |
| **dotenv**          | Secure environment configuration |
| **HTML (Jinja2)**   | Templating for views             |

---

## 🚩 Features

* ✅ Add new user
* ✅ View all users
* ✅ Edit existing user
* ✅ Delete user
* ✅ Display current date and time
* ✅ Simple number addition via form

---

## 📂 Project Structure

```
├── app.py                 # Main Flask Application
├── .env                   # Environment variables for MySQL credentials
├── templates/              # HTML Templates (Jinja2)
│   ├── index.html
│   ├── adduser.html
│   ├── edituser.html
│   ├── date.html
│   ├── sum.html
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.9+
* MySQL Server (Running on `localhost:3306`)

### 🔨 Installation Steps

1️⃣ Clone the Repository

```bash
git clone https://github.com/lovnishverma/flask-mysql-crud-app.git
cd flask-mysql-crud-app
```

2️⃣ Set up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux / macOS
venv\Scripts\activate         # On Windows
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Configure `.env` for MySQL Credentials

```
user=your_mysql_username
pass=your_mysql_password
```

5️⃣ Ensure MySQL is Running

* Port: `3306`
* Host: `localhost`
* User exists with the credentials provided in `.env`

6️⃣ Run the Application

```bash
python app.py
```

7️⃣ Open in Browser

```
http://localhost:5000
```

---

## 💡 Usage Instructions

| URL            | Purpose              |
| -------------- | -------------------- |
| `/`            | List all users       |
| `/adduser`     | Form to add user     |
| `/edit/<id>`   | Edit specific user   |
| `/delete/<id>` | Delete specific user |
| `/date`        | Show current date    |
| `/sumpage`     | Sum numbers via form |

---


## 📢 Disclaimer

> This project is created **strictly for educational purposes only**.
> It is not intended for production usage. Security best practices such as input validation, CSRF protection, authentication, and authorization are not implemented.
> The database schema is minimal and the project structure is kept simple for easier understanding.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧑‍🏫 Acknowledgements

* [Flask Documentation](https://flask.palletsprojects.com/)
* [MySQL Documentation](https://dev.mysql.com/doc/)
* [Python dotenv](https://pypi.org/project/python-dotenv/)

---

## ⭐ How to Support

If you found this project useful for learning:

* ⭐ Star this repository
* ✅ Fork and experiment further
* 💬 Share feedback for improvement

---

