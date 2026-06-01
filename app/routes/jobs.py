from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app import models,schemas
from app.auth import get_current_user
router=APIRouter(prefix="/jobs",tags=["jobs"])
from app.ai import tailor_resume
from app.ai import generate_interview_questions
@router.get("/")
def get_all_jobs(db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    jobs=db.query(models.Job).filter(models.Job.user_id==current_user["user_id"]).all()
    return jobs

@router.get("/{job_id}")
def get_one_job(job_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    job=db.query(models.Job).filter(models.Job.user_id==current_user["user_id"]).filter(models.Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="Job not found")
    return job

@router.post("/")
def create_job(job:schemas.JobCreate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    new_job=models.Job(
        user_id=current_user["user_id"],
        company=job.company,
        role=job.role,
        status=job.status,
        notes=job.notes,
        job_description=job.job_description
    )   
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.delete("/{job_id}")
def delete_job(job_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    job=db.query(models.Job).filter(models.Job.user_id==current_user["user_id"]).filter(models.Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="Job  not found ")
    db.delete(job)
    db.commit()
    return {"message:"f"Job {job_id} deleted successfully"}

@router.put("/{job_id}")
def update_job(job_id:int,job_data:schemas.JobUpdate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    job=db.query(models.Job).filter(models.Job.user_id==current_user["user_id"]).filter(models.Job.id==job_id).first()
    if not job:
        raise HTTPException(status_code=404,detail="Job not found")
    for key,value in job_data.model_dump(exclude_unset=True).items():
        setattr(job,key,value)
    db.commit()
    db.refresh(job)
    return job

@router.post("/{job_id}/tailor-resume")
def tailor_job_resume(job_id:int,resume_input:schemas.Resume_Input,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    job=db.query(models.Job).filter(models.Job.id==job_id,models.Job.user_id==current_user["user_id"]).first()
    if not job:
        raise HTTPException(status_code=404,detail="Job not found")
    if not job.job_description:
        raise HTTPException(status_code=400,detail="No job description found for this job")
    tailored=tailor_resume(job.job_description,resume_input.resume_bullets)
    return {"tailored_resume":tailored}

@router.post("/{job_id}/interview_questions")
def interview_questions(job_id:int,resume_input:schemas.Resume_Input,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    job=db.query(models.Job).filter(models.Job.id==job_id,models.Job.user_id==current_user["user_id"]).first()
    if not job:
        raise HTTPException(status_code=404,detail="job not found")
    if not job.job_description:
        raise HTTPException(status_code=400,detail="No job decription found for this job")
    Questions=generate_interview_questions(job.job_description,resume_input.resume_bullets)
    return {"Interview Questions": Questions}