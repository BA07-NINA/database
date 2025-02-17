import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.models import Base, Deployment
from src.db import engine, get_db

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the backend!"}

@app.get("/deployments/")
def get_deployments(db: Session = Depends(get_db)):
    return db.query(Deployment).all()
