# Monitoring System Dashboard

A full-stack real-time monitoring dashboard built using Python, FastAPI, Next.js, Tailwind CSS, SQLite, Docker, and Recharts.

This project demonstrates:

* Backend Engineering
* REST API Development
* Authentication & JWT Basics
* Database Integration
* Real-Time Monitoring
* Frontend Dashboard Development
* Docker & DevOps Fundamentals

---

# Features

## Backend (FastAPI)

* Real-time CPU monitoring
* RAM monitoring
* Historical metrics storage
* SQLite database integration
* JWT authentication basics
* Modular backend architecture
* REST API endpoints
* Dockerized backend

## Frontend (Next.js)

* Real-time monitoring dashboard
* Live auto-refreshing metrics
* Historical charts using Recharts
* Responsive UI with Tailwind CSS
* API integration with FastAPI
* Dockerized frontend

---

# Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* psutil
* python-jose
* passlib
* bcrypt

## Frontend

* Next.js
* React
* Tailwind CSS
* Recharts

## DevOps

* Docker
* Docker Compose

---

# Project Structure

```txt
monitoring-project/
│
├── backend/
│   └── monitoring-system/
│       │
│       ├── app/
│       │   ├── auth/
│       │   ├── models/
│       │   ├── routes/
│       │   ├── schemas/
│       │   ├── services/
│       │   ├── database.py
│       │   └── main.py
│       │
│       ├── Dockerfile
│       ├── requirements.txt
│       └── monitoring.db
│
├── frontend/
│   └── monitoring-dashboard/
│       │
│       ├── src/
│       │   ├── app/
│       │   └── components/
│       │
│       ├── Dockerfile
│       ├── package.json
│       └── next.config.ts
│
└── docker-compose.yml
```

---

# Installation

## Prerequisites

Install the following:

* Python 3.12+
* Node.js 20+
* Docker Desktop
* Git

---

# Backend Setup

Navigate to backend:

```bash
cd backend/monitoring-system
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

## Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psutil python-jose passlib bcrypt==4.0.1 python-multipart
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```txt
http://127.0.0.1:8000
```

Swagger Docs:

```txt
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend/monitoring-dashboard
```

Install dependencies:

```bash
npm install
```

Install chart library:

```bash
npm install recharts
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```txt
http://localhost:3000
```

---

# Docker Setup

## Build Backend

```bash
cd backend/monitoring-system

docker build -t monitoring-backend .
```

Run backend container:

```bash
docker run -p 8000:8000 monitoring-backend
```

---

## Build Frontend

```bash
cd frontend/monitoring-dashboard

docker build -t monitoring-frontend .
```

Run frontend container:

```bash
docker run -p 3000:3000 monitoring-frontend
```

---

# Docker Compose

Run full stack:

```bash
docker compose up --build
```

---

# API Endpoints

## Metrics

### Get Live Metrics

```http
GET /metrics
```

---

### Get Metrics History

```http
GET /history
```

---

## Authentication

### Register User

```http
POST /register
```

Example:

```json
{
  "username": "Ishan",
  "email": "ishan@gmail.com",
  "password": "12345"
}
```

---

### Login User

```http
POST /login
```

Example:

```json
{
  "email": "ishan@gmail.com",
  "password": "12345"
}
```

---

# Common Errors & Fixes

## 1. ModuleNotFoundError: No module named 'app'

### Cause

Running uvicorn from wrong folder.

### Fix

Navigate into:

```txt
backend/monitoring-system
```

Then run:

```bash
uvicorn app.main:app --reload
```

---

## 2. ModuleNotFoundError: No module named 'passlib'

### Cause

Virtual environment not activated.

### Fix

Activate venv:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

## 3. bcrypt Error

Example:

```txt
error reading bcrypt version
```

### Fix

Install compatible version:

```bash
pip install bcrypt==4.0.1
```

---

## 4. requirements.txt Empty

### Cause

Generated outside virtual environment.

### Fix

Activate venv first:

```bash
.venv\Scripts\activate
```

Then regenerate:

```bash
pip freeze > requirements.txt
```

---

## 5. chartData.slice is not a function

### Cause

Frontend expected array but backend returned object/error.

### Fix

Ensure `/history` endpoint returns list data.

---

## 6. Failed to fetch

### Cause

Backend server not running.

### Fix

Run backend:

```bash
uvicorn app.main:app --reload
```

---

## 7. Docker uvicorn executable not found

### Cause

requirements.txt missing uvicorn.

### Fix

Install uvicorn:

```bash
pip install uvicorn
```

Regenerate requirements:

```bash
pip freeze > requirements.txt
```

Rebuild Docker image:

```bash
docker build -t monitoring-backend .
```

---

## 8. Virtual Environment Broken After Moving Project

### Cause

Project folder moved to different path.

### Fix

Delete `.venv` and recreate:

```bash
python -m venv .venv
```

---

## 9. CORS Errors

### Cause

Frontend and backend are different origins.

### Fix

Add CORSMiddleware in FastAPI.

# Author

TDeveloped by Kavinda Sandaru
