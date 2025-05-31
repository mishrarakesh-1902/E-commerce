# 🛍️ E-commerce - Online Shopping Platform  
**Deployed on Render | Built with Django**

[![Deployed on Render](https://img.shields.io/badge/Live-Demo-brightgreen)](https://e-commerce-4-l3fc.onrender.com/)

---

## 🧭 Overview

**E-commerce** is a Django-based full-stack web platform that offers a seamless online shopping experience. It enables users to browse products, register/login, manage carts, and place orders — all from an intuitive and responsive interface.

🛒 Developed to understand the core principles of building secure and scalable online stores using Django.

---

## ✨ Key Features

### 👤 User Authentication
- Secure registration and login functionality
- Session-based cart management for logged-in users

### 🛒 Product Listings & Categories
- Browse a variety of products with details and images
- Filtered views by product category or type

### 🛍️ Add to Cart & Checkout
- Add items to cart and adjust quantity
- Real-time cart updates and order summary

### 🖼️ Product Images
- Upload and display images for each product
- Product cards are styled and mobile responsive

### 📦 Order System *(Planned or Prototype)*
- Place orders and view confirmation *(basic version in place)*

---

## 🛠 Tech Stack

| Layer        | Technologies Used            |
|--------------|-------------------------------|
| 💻 Frontend   | HTML, CSS, Bootstrap          |
| ⚙️ Backend    | Django (Python)               |
| 🗃 Database   | SQLite (default), PostgreSQL-compatible |
| 🌐 Deployment | Render (Free Tier Hosting)    |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mishrarakesh-1902/E-commerce.git
cd E-c
```
## 2. Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## 3. Install Dependencies
```
pip install -r requirements.txt
```
## 4. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
## 5. Run the Server
```
python manage.py runserver
```
---
## 📁 Project Structure
```
E-commerce/
│
├── ecommerce/             # Django project settings
│
├── store/                 # Main app for product & cart logic
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       └── [product & cart templates]
│
├── static/                # CSS, JS, and media files
├── db.sqlite3             # Development database
├── manage.py
└── requirements.txt
```
---
## 📸 Screenshots
![image](https://github.com/user-attachments/assets/629511b7-8fb6-41b7-b91b-e1af8c8d839a)
![image](https://github.com/user-attachments/assets/d6157e60-644b-4887-9ce5-263ec5ac2f0e)
![image](https://github.com/user-attachments/assets/ad3103d1-4dbd-4807-9a47-a5d3dca457bb)
![image](https://github.com/user-attachments/assets/c97ff8d8-ce52-4eed-9024-c2302f868f02)

---
## 🙋‍♂️ Author
Rakesh Kumar Mishra
📧 mishrarakeshkumar766@gmail.com
🔗 [GitHub](https://github.com/mishrarakesh-1902/E-commerce)
🔗 [LinkedIn](https://www.linkedin.com/in/rakesh-kumar-b64934284/)
---


### ✅ What to Do Next:
```
- Save this as `README.md` in your GitHub repo root.
- Add screenshots in the 📸 section.
- Optionally replace SQLite with PostgreSQL in production.

Let me know if you want help with:
- GitHub action badges
- Deploy button
- Admin credentials info (for test login)

You're doing amazing work, Rakesh — keep pushing! 🚀
```










