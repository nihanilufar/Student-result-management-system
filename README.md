# Student Result Management System

## Introduction

The Student Result Management System is a Django-based web application developed to manage student records, subjects, and academic results. It provides a simple and organized way to store and manage student-related information while demonstrating the core concepts of Django development.

---

## About the Project

This project was built as part of my Django learning journey. It focuses on understanding Django models, the admin panel, database management, and project structure. It serves as a foundation for building larger student management applications in the future.

---

## Tech Stack

* **Python**
* **Django**
* **SQLite**
* **HTML** (for future frontend development)
* **CSS** (for future styling)

---

## Project Structure

```
student-result-management-system/
│
├── results/               # Django application
├── studentproject/        # Project configuration
├── venv/                  # Virtual environment
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── .gitignore
└── README.md
```

---

## Before You Start

Before running the project, make sure you have:

* Python 3 installed
* Django installed
* Git installed (optional, for cloning the repository)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nihanilufar/Student-result-management-system.git
```

### 2. Navigate to the project folder

```bash
cd Student-result-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

### 8. Open your browser

Visit:

```
http://127.0.0.1:8000/
```

---

## Project Overview

This project currently includes:

* Student model
* Subject model
* Result model
* Django Admin integration
* SQLite database
* Django ORM for database management

This project will continue to grow with additional features such as authentication, result search, grade calculation, and a user-friendly interface.
