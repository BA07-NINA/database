from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

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