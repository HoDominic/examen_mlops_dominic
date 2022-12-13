
from schemas.Course import Course
from fastapi import APIRouter
from fastapi import FastAPI,HTTPException





#APIROUTER
router = APIRouter(prefix="/course",
tags=["Course"],
responses={404: {"Patient": "Not found"}},
)
