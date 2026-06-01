import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def tailor_resume(job_description:str,resume_bullets:str)->str:
    prompt=f"""you are professional resume writer helping a job seeker.

Job Description:
{job_description}

Current Resume Bullets:
{resume_bullets}

Rewrite the resume bullets to:
1. Match the language and keywords in the job description
2. Highlight relevant skills the JD is asking for
3. Keep bullets concise and achievement-focused
4. Return ONLY the rewritten bullets, nothing else
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_interview_questions(job_description:str,resume_bullets:str)->str:
    prompt=f"""You are a professional recruiter and interview helping a job seeker.Given the job description and resume below

    Job Description:
    {job_description}

    Resume Bullets:
    {resume_bullets},
   generate 10 likely interview questions the interviewer would ask.
   Include a mix of technical questions based on the JD requirements and behavioral questions based on the candidate's experience. 
   Return only the questions as a numbered list, nothing else.
    


"""
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content