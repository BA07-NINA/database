from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

class Observation(Base):
    __tablename__ = "observation"
    eventID = Column(String, primary_key=True)
    mediaID = Column(String, ForeignKey("media.mediaID"), nullable=False)
    info = Column(String(100))
    time_start = Column(TIMESTAMP)
    time_end = Column(TIMESTAMP)

    media = relationship("Media", back_populates="observations")