from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    created_at = Column(DateTime, server_default=func.now())
class Job(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,nullable=False)
    company=Column(String,nullable=False)
    role=Column(String,nullable=False)
    status=Column(String,default="Applied")
    notes=Column(String,nullable=True)
    job_description=Column(String,nullable=True)
    applied_date=Column(DateTime,server_default=func.now())
