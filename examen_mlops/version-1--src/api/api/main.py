from glob import glob
from typing import List
import json
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.Course import Course
from retry import retry


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@retry(delay=2)
def read_in_all_courses(limit: int = -1) -> List[Course]:
    """
    This function will read in all the data from the 'data' folder containing JSON files.
    Make sure to Parse them into Courses using Pydantic Schema's.
    Append them to the all_courses list and return that list."""

    all_courses = []
    for course in glob(f'data/*.{os.environ.get("file_format", "md")}')[:limit]:
        try:
            with open(course, 'r') as f:
                courseParsed = json.load(f)
                key = list(courseParsed.keys())[0]
                all_courses.append(Course(**courseParsed[key]))
        except Exception as e:
            print('Error with file', course)
    return all_courses

all_courses = read_in_all_courses(-1)

@app.get("/")
async def root():
    return {"message": "I am working correctly!"}

@app.get("/docker_test")
async def docker_test():
    return os.environ

@app.get('/mct/courses')
async def get_all_courses():
    return all_courses