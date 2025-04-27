from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    filepath = Column(String)
    filetype = Column(String)
    filesize = Column(Integer)
    upload_time = Column(DateTime, default=datetime.utcnow)
