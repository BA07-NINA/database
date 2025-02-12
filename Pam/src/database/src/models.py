from sqlalchemy import create_engine, Column, String, Integer, Float, Text, ForeignKey, Boolean, DECIMAL, TIMESTAMP, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Deployment(Base):
    __tablename__ = "deployment"
    deploymentID = Column(String, primary_key=True)
    deviceID = Column(String, ForeignKey("device.deviceID"), nullable=False)
    latitude = Column(DECIMAL(9, 6), nullable=False)
    longitude = Column(DECIMAL(9, 6), nullable=False)
    date_start = Column(TIMESTAMP, nullable=False)
    date_end = Column(TIMESTAMP, nullable=True)
    notes = Column(Text)

    media = relationship("Media", back_populates="deployment")

class Media(Base):
    __tablename__ = "media"
    mediaID = Column(String, primary_key=True)
    deploymentID = Column(String, ForeignKey("deployment.deploymentID"), nullable=False)
    configuration = Column(Text)
    timestamp = Column(TIMESTAMP)
    file_path = Column(String(255))
    size_MB = Column(DECIMAL(10, 2))

    deployment = relationship("Deployment", back_populates="media")
    observations = relationship("Observation", back_populates="media")
    annotations = relationship("Annotation", back_populates="media")
    sound_quality = relationship("SoundQuality", uselist=False, back_populates="media")

class Observation(Base):
    __tablename__ = "observation"
    eventID = Column(String, primary_key=True)
    mediaID = Column(String, ForeignKey("media.mediaID"), nullable=False)
    info = Column(String(100))
    time_start = Column(TIMESTAMP)
    time_end = Column(TIMESTAMP)

    media = relationship("Media", back_populates="observations")

class Device(Base):
    __tablename__ = "device"
    deviceID = Column(String, primary_key=True)
    device_name = Column(String(100))
    info = Column(String(100))

class SoundQuality(Base):
    __tablename__ = "sound_quality"
    mediaID = Column(String, ForeignKey("media.mediaID"), primary_key=True)
    quality_score = Column(Integer)
    noise_level = Column(DECIMAL(5, 2))

    media = relationship("Media", back_populates="sound_quality")

class Annotation(Base):
    __tablename__ = "annotation"
    annotationID = Column(String, primary_key=True)
    mediaID = Column(String, ForeignKey("media.mediaID"), nullable=False)
    annotation_type = Column(String(50))
    text = Column(Text)
    timestamp = Column(TIMESTAMP)

    media = relationship("Media", back_populates="annotations")

class User(Base):
    __tablename__ = "user"
    userID = Column(String, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50))
