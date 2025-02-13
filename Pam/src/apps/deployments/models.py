import datetime
from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

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