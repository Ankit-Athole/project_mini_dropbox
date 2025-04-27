from sqlalchemy.orm import Session
from app.models.file import File
from app.schemas.file import FileCreate

def save_file(db: Session, file_data: FileCreate):
    db_file = File(**file_data.dict())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_all_files(db: Session):
    return db.query(File).all()

def get_file_by_id(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()
