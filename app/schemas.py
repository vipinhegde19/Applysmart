from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str
    @field_validator("password")
    def password_length(cls, value):
        if len(value) > 72:
            raise ValueError("Password cannot be longer than 72 characters")
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class JobCreate(BaseModel):
    company:str
    role:str
    status:Optional[str]="Applied"
    notes:Optional[str]=None
    job_description:Optional[str]=None

class JobUpdate(BaseModel):
    company:Optional[str]=None
    role:Optional[str]=None
    status:Optional[str]=None
    notes:Optional[str]=None
    job_description:Optional[str]=None

class Resume_Input(BaseModel):
    resume_bullets:str