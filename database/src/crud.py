from sqlalchemy.orm import Session
from models import (
    Deployment,
    Media,
    Observation,
    Device,
    SoundQuality,
    Annotation,
    User,
)


# ------------------- Deployment -------------------
def create_deployment(db: Session, deployment: Deployment):
    db.add(deployment)
    db.commit()
    db.refresh(deployment)
    return deployment


def get_deployment_by_id(db: Session, deployment_id: str):
    return db.query(Deployment).filter(Deployment.deploymentID == deployment_id).first()


def get_all_deployments(db: Session):
    return db.query(Deployment).all()


def delete_deployment(db: Session, deployment_id: str):
    deployment = get_deployment_by_id(db, deployment_id)
    if deployment:
        db.delete(deployment)
        db.commit()
    return deployment


# ------------------- Media -------------------
def create_media(db: Session, media: Media):
    db.add(media)
    db.commit()
    db.refresh(media)
    return media


def get_media_by_id(db: Session, media_id: str):
    return db.query(Media).filter(Media.mediaID == media_id).first()


def get_all_media(db: Session):
    return db.query(Media).all()


def delete_media(db: Session, media_id: str):
    media = get_media_by_id(db, media_id)
    if media:
        db.delete(media)
        db.commit()
    return media


# ------------------- Observation -------------------
def create_observation(db: Session, observation: Observation):
    db.add(observation)
    db.commit()
    db.refresh(observation)
    return observation


def get_observation_by_id(db: Session, event_id: str):
    return db.query(Observation).filter(Observation.eventID == event_id).first()


def get_observations_by_media(db: Session, media_id: str):
    return db.query(Observation).filter(Observation.mediaID == media_id).all()


# ------------------- Device -------------------
def create_device(db: Session, device: Device):
    db.add(device)
    db.commit()
    db.refresh(device)
    return device


def get_device_by_id(db: Session, device_id: str):
    return db.query(Device).filter(Device.deviceID == device_id).first()


def get_all_devices(db: Session):
    return db.query(Device).all()


# ------------------- Sound Quality -------------------
def create_sound_quality(db: Session, sound_quality: SoundQuality):
    db.add(sound_quality)
    db.commit()
    db.refresh(sound_quality)
    return sound_quality


def get_sound_quality_by_media(db: Session, media_id: str):
    return db.query(SoundQuality).filter(SoundQuality.mediaID == media_id).first()


# ------------------- Annotation -------------------
def create_annotation(db: Session, annotation: Annotation):
    db.add(annotation)
    db.commit()
    db.refresh(annotation)
    return annotation


def get_annotation_by_id(db: Session, annotation_id: str):
    return db.query(Annotation).filter(Annotation.annotationID == annotation_id).first()


def get_annotations_by_media(db: Session, media_id: str):
    return db.query(Annotation).filter(Annotation.mediaID == media_id).all()


# ------------------- User -------------------
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.userID == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_all_users(db: Session):
    return db.query(User).all()

