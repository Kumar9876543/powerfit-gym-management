# 🏋️ PowerFit Gym Management System

A full-stack Gym Management Web Application built using Django.  
This system helps manage gym members, membership plans, trainers, and contact inquiries with proper role-based access control.

---

## 🚀 Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL (Development)
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Authentication System
- **Version Control:** Git & GitHub

---

## ✨ Features

### 🔐 Authentication & Authorization
- Admin Login
- Staff Login
- Secure logout system
- Role-based access control

### 👥 Member Management
- Add new members
- Update member details
- Delete members
- View all members
- Membership expiry tracking

### 📦 Membership Plans
- Basic Plan
- Premium Plan
- VIP Plan
- Plan duration & pricing management

### 📬 Contact Form
- Users can send inquiries
- Messages stored in database
- Admin can view submitted messages

### 📊 Admin Dashboard
- View total members
- Track active memberships
- Manage plans and users

---

## 🧠 Project Architecture

The application follows Django’s MVT (Model-View-Template) architecture:

1. User sends request
2. URL routes request to View
3. View interacts with Model
4. Model communicates with Database
5. Response rendered via Template
6. Output sent back to user

---

## 🗂 Project Structure
PowerFitGym/
│
├── manage.py
├── requirements.txt
├── PowerFitGym/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── gym/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/


---

## ⚙️ How to Run Locally

1. Clone the repository:
git clone https://github.com/Kumar9876543/powerfit-gym-management.git

2. Navigate to project folder:
cd powerfit-gym-management
3. Create virtual environment:


python -m venv venv


4. Activate virtual environment:


venv\Scripts\activate


5. Install dependencies:


pip install -r requirements.txt


6. Run migrations:


python manage.py migrate


7. Start server:


python manage.py runserver


---

## 📸 Screenshots


![Home Page](home.png)
![about Page](about.png)
![add member Page](screenshots/add member.png)
![contact](contact.png)
![login](login.png)
![member_list](member_list.png)


---

## 🎯 Learning Outcomes

- Implemented Django authentication system
- Designed relational database models
- Handled CRUD operations
- Implemented role-based authorization
- Connected backend with database
- Managed full project lifecycle using Git

---

## 👨‍💻 Author

Vinay Kumar  
BTech CSE | Python Full Stack Developer  
Focused on building scalable web applications using Django.
