from glob import glob
from typing import List
import json
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.Course import Course
from retry import retry


#router
from routers import (
    course_router as course # Just to make an alias, because it looks nicer.
    
)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(course.router)