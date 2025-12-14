## Project Overview

The Sweet Shop Management System is a **full-stack, test-driven application** designed to manage sweets in a shop.  
It allows users to **register, login, browse, search, and purchase sweets**, while admins can **add, update, delete, and restock** sweets.  

This project demonstrates skills in:

- **Backend API development** with Python (FastAPI)
- **Database management** using MongoDB
- **Frontend development** with a modern SPA framework (React)
- **Test-Driven Development (TDD)**
- **Clean coding and version control practices**
- **AI-assisted development responsibly**

---

## Features

### User Features
- Register and login
- Browse all available sweets
- Search sweets by name, category, or price range
- Purchase sweets (quantity decreases automatically)
- Responsive and user-friendly UI

### Admin Features
- Add new sweets
- Update existing sweets
- Delete sweets
- Restock sweets
- Full control over inventory

### API Endpoints

#### Auth
- `POST /api/auth/register` – Register a new user
- `POST /api/auth/login` – Login and receive JWT token

#### Sweets (Protected)
- `POST /api/sweets` – Add a new sweet
- `GET /api/sweets` – List all sweets
- `GET /api/sweets/search` – Search sweets by filters
- `PUT /api/sweets/:id` – Update sweet details
- `DELETE /api/sweets/:id` – Delete a sweet (Admin only)

#### Inventory (Protected)
- `POST /api/sweets/:id/purchase` – Purchase a sweet
- `POST /api/sweets/:id/restock` – Restock a sweet (Admin only)

---

## Setup Instructions

### Prerequisites
- Node.js >= 18 (for frontend if React)
- Python >= 3.10 (for backend)
- MongoDB installed locally or MongoDB Atlas account
- Git

---

### Backend Setup (FastAPI)

1. Open terminal and navigate to backend folder:


cd "C:\Users\prano\Sweet Shop Management System\backend"

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload


### Frontend Setup 

cd "C:\Users\prano\Sweet Shop Management System\frontend"
npm install
npm start
http://localhost:3000




### Login/Register Page
Dashboard / Sweets Listing
Add / Update Sweet (Admin)


### AI Usage

I used AI tools to accelerate development and maintain code quality. Below is a summary:

###Tools Used

ChatGPT – Assisted with generating boilerplate code, writing test cases, and debugging issues.

GitHub Copilot – Suggested snippets for repetitive tasks like API endpoint structures and frontend UI components.
