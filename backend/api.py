from fastapi import FastAPI
from pydantic import BaseModel

import logger, db

app = FastAPI()

class JobInput(BaseModel):
    job_type: str
    job_input: str

class JobOutput(BaseModel):
    job_id: str
    job_type: str
    state: str

@app.get("/jobs")
def get_jobs():
    '''
    This gets all the jobs as a list in format of JobOutput
    '''
    
    return {"GET jobs": "List of jobs"}

@app.post("/jobs")
def create_job(job: JobInput):
    '''
    Using the JobInput model we will be given some info and send it to our worker class
    Since we don't have a backend yet, will just use curl 
    '''
    
    return {"message": "Sending job"}

@app.get("/jobs/{job_id}")
def get_job_id(job_id):
    '''
    With the parameter job_id we will use that and get the status and information about that job and expect an output like the JobOutput Model
    '''
    return {"job_id": f"{job_id}"}

@app.get("/health")
def get_health():
    '''
    Gives us info about the API and if its alive or not
    '''
    return {"health": "soon to be alive"}