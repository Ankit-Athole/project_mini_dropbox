# Mini Dropbox - Fullstack Project

This is a fullstack mini Dropbox clone where users can upload, list, view, and download files.

---

## Tech Stack

- **Backend:** FastAPI + SQLite
- **Frontend:** React.js + Tailwind CSS + Toastify

---

## Features

- Upload files (.txt, .jpg, .png, .json)
- List all uploaded files
- View and download files
- Toast notifications for success/error

---


---

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
    ```bash
    cd backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the backend server:
    ```bash
    uvicorn app.main:app --reload
    ```

The server will start at: [http://localhost:8000](http://localhost:8000)

---

### Frontend Setup

1. Navigate to frontend directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the frontend development server:
    ```bash
    npm start
    ```

Frontend will run at: [http://localhost:3000](http://localhost:3000)

---

## APIs Available

- **POST** `/upload` → Upload a file
- **GET** `/files` → Get list of all files
- **GET** `/files/{file_id}` → Download file by ID

---


