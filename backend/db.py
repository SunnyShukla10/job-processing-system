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
import uuid
import datetime
import sqlite3
from typing import Optional

    
# Job creation and lookup
def create_job(job_type, job_input) -> str:
    '''
    Docstring for create_job
    
    Responsibilities:
    - Assigns job_id
    - Sets created_at
    - Adds to the db
    '''

    job_id = uuid.uuid4()
    state = "pending"
    created_at = datetime.datetime.now().isoformat()
    
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO jobs (job_id, job_type, job_input, state, created_at) VALUES (?,?,?,?,?)", (str(job_id),job_type,job_input,state,created_at))      

    return str(job_id)

def get_job(job_id):
    '''
    Docstring for get_job
    
    Fethes the job given a job_id

    Read only op
    Used by API to report status
    '''
    conn = sqlite3.connect(config.DB_PATH)
    cur = conn.cursor()
    row = cur.execute("SELECT job_type, state FROM jobs WHERE job_id = ?", (job_id,)).fetchone()

    if row:
        job_type, state = row[0], row[1]

        return (job_type, state)

    return None


def get_all_jobs():
    '''
    Docstring for get_all_jobs
        
    Fetches all jobs and returns a list of them
    
    '''
    pass

# Job claiming
def claim_next_job() -> Optional[str]:
    '''
    Docstring for claim_next_job
    
    Atomically claim a single pending job

    Responsibilities:
    - Select one pending job
    - Transition the state
    - Set started_at

    Returns the claimed job or None if no jobs are avaliable
    
    '''
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()

        row = cur.execute("SELECT job_id FROM jobs WHERE state = 'pending' ORDER BY created_at LIMIT 1").fetchone()
        if row:
            job_id = row[0]
            started_at = datetime.datetime.now().isoformat()
            cur.execute("UPDATE jobs SET state = 'running', started_at = ? WHERE job_id = ? AND state = 'pending'", (started_at,job_id))

            return job_id if cur.rowcount == 1 else None

        return None

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