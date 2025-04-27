from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import file as models
from app.schemas import file as schemas
from app.crud import file_crud
import shutil
import os

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "./uploads/"
ALLOWED_TYPES = {"text/plain", "image/jpeg", "image/png", "application/json"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload", response_model=schemas.FileResponse)
async def upload_file(uploaded_file: UploadFile = File(...), db: Session = Depends(get_db)):
    if uploaded_file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="File type not allowed.")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    file_data = schemas.FileCreate(
        filename=uploaded_file.filename,
        filepath=file_path,
        filetype=uploaded_file.content_type,
        filesize=os.path.getsize(file_path)
    )

    return file_crud.save_file(db, file_data)

@router.get("/files", response_model=list[schemas.FileResponse])
def list_files(db: Session = Depends(get_db)):
    return file_crud.get_all_files(db)

@router.get("/files/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = file_crud.get_file_by_id(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    return {"download_url": file.filepath}
