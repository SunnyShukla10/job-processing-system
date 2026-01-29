'''
Docstring for job-processing-system.backend.db

This is the source of truth for job persistence and state transitions:

This contains:
- Job model
- Job state machines and invariants

All job state transitions must go through this file

'''


# Job states and transitions

'''
Job States:
- pending
- running
- completed
- failed

Allowed transitions
- pending -> running 
- running -> completed
- running -> failed
- failed -> pending (only during retries as long as the count < max-retry)
'''
import logger
import config


# Job data model

class Job:
    job_id: str
    job_type: str
    job_input: str
    state: str 
    created_at: str
    started_at: str
    finished_at: str
    result: str
    error: str
    


# Job creation and lookup

def create_job(job_type, job_input):
    '''
    Docstring for create_job
    
    Responsibilities:
    - Assigns job_id
    - Sets created_at
    - Adds to the db
    '''
    pass

def get_job(job_id):
    '''
    Docstring for get_job
    
    Fethes the job given a job_id

    Read only op
    Used by API to report status
    '''

def get_all_jobs():
    '''
    Docstring for get_all_jobs
        
    Fetches all jobs and returns a list of them
    
    '''
    pass

# Job claiming
def claim_next_job():
    '''
    Docstring for claim_next_job
    
    Atomically claim a single pending job

    Responsibilities:
    - Select one pending job
    - Transition the state
    - Set started_at

    Returns the claimed job or None if no jobs are avaliable
    
    '''
    pass


# Job completion/faliure

def mark_job_completed(job_id, result):
    '''
    Docstring for mark_job_completed
    
    Mark a running job as completed

    Responsibilities:
    - validate curr state is running
    - set result
    - set finished_at

    Invalid transitions must be rejected
    '''

    pass

def mark_job_failed(job_id, error):
    '''
    Docstring for mark_job_failed
    
    Mark a running job as failed

    '''