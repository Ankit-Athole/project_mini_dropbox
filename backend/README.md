# Backend - Mini Dropbox Project

This backend server is built using FastAPI and uses SQLite database to manage file uploads.

---

## Features

- Upload file API
- List all files API
- Download file API
- Stores metadata like filename, type, size, upload time

---

## Tech Stack

- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy

---

## Setup Instructions

1. Navigate to backend directory:
    ```bash
    cd backend
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the server:
    ```bash
    uvicorn app.main:app --reload
    ```

---

## API Endpoints

| Method | URL | Description |
|:-------|:----|:------------|
| POST | `/upload` | Upload a file |
| GET | `/files` | Get list of uploaded files |
| GET | `/files/{file_id}` | Get a download link for a specific file |

---
