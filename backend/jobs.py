'''
Docstring for job-processing-system.backend.jobs

Contains job execution logic

This maps job types to execution functions and runs them

Given a job_type and job_input, it either:
- returns a result
- raises an exectpion
'''

def execute_job(job_type, job_id):
    '''
    Docstring for execute_job
    
    Executes a job based on type

    Responsibilites:
    - Validates job_type
    - Dispatches to correct job_handler
    - Returns result or raises exception
    '''

    pass

# Job handlers

def _run_job_1(job_input):
    '''
    Docstring for _run_job_1
    
    Runs job1 (need to figure out what jobs it may be)

    Ex) Reading a file
    '''
    pass

def _run_job_2(job_input):
    '''
    Docstring for _run_job_2
    
    Runs job1 (need to figure out what jobs it may be)

    Ex) Getting contents of a file
    '''
    pass