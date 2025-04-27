from pydantic import BaseModel
from datetime import datetime

class FileBase(BaseModel):
    filename: str
    filepath: str
    filetype: str
    filesize: int

class FileCreate(FileBase):
    pass

class FileResponse(FileBase):
    id: int
    upload_time: datetime

    class Config:
        orm_mode = True
