from sqlalchemy.orm import Session
from src.models import Deployment

def get_all_deployments(db: Session):
    return db.query(Deployment).all()

def create_deployment(db: Session, deployment: Deployment):
    db.add(deployment)
    db.commit()
    db.refresh(deployment)
    return deployment
