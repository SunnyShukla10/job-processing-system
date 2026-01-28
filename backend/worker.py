'''
Docstring for job-processing-system.backend.worker

This looks for pending jobs and executes them

- Runs in a long lived worker loop
- Claims jobs using the db.py
- Executes job logic using jobs.py
'''
import time

import db
import jobs
import config

# Worker loop

def run_worker():
    '''
    Docstring for run_worker

    Main worker loop

    Responsibilities:
    - Keeps polling for avaliable jobs
    - Claims one job at at ime 
    - Executes job logic
    '''
    pass

# Job processing

def _process_job(job):
    '''
    Docstring for _process_job
    
    Executes single claimed job

    '''

    pass

# Idle
def _sleep_when_idle():
    '''
    Docstring for _sleep_when_idle
    
    Sleeps when no jobs are avliable

    Reduces DB load and CPU usage
    '''
    pass