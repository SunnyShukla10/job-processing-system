# Job Processing System 

## Overview

This project is meant to understand how real backend systems process running jobs asynchrously while remaining reliable. It is focuses on job state modeling, It focuses on reliable job persistence, asynchronous processing, retries, and failure recovery using a database as the source of truth.


### Overall Flow

Clients will send long-running tasks to the API as jobs.
Jobs are persisted in the databse and will be done asynchrously by one of more workers.

Workers will poll the databse and try to find pending jobs, claim them atomically, execute the job, and store information about them throughout they run. 

The database will be the source of truth as it will coordinate work betwween workers.


## Structure 

### API

A FastAPI backend that is respobsible for job creation, jobs retrival, and job state retrivale.
The API never executes jobs and only acts as an interface for submitting work and querying jobs. 

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/jobs` | POST | Create a job |
| `/jobs` | GET | List of all job |
| `/jobs/{job_id}` | GET | Retrieve job status | 

### Worker

This does the work of the jobs. It uses the database to find pending jobs and execute them and other functionalities.

### Database

****Schema**** 

A Job stores:
- job_id
- job_type
- state
- created_at
- updated_at
- started_at
- finished_at
- result (success only)
- error (failure only)


### Invariants

**Job States**

A job can be in one of the following states:
- pending
- running
- completed
- failed

Only valid state transitions:
* pending -> running -> failed
* pending -> running -> completed

**Schema**

Write-once fields:  
    - job_type  
    - job_id  
    - created_at  
    - started_at  
    - finished_at  
  
Mutable fields:  
    - state  
    - updated_at  
    
  
Other Invariants:  
    - result is set iff state is completed  
    - error is set iff there was an error


## Job Claiming Semantics

Job can be claimed if current state is oending and it hasn't been claimed by worker.
With the usage of a database, if multiple workers attempt to claim the same job, only one gets it and the others move on.


## Guarantees (v1)

* Jobs are never executed more than once concurrently.
* Job state transitions are forward-only and persisted.
* Worker and API crashes do not corrupt job state.
* Duplicate job creation is possible and documented.
* Recovery is based on timeouts and retry limits.