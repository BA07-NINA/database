from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base


class SoundQuality(Base):
    __tablename__ = "sound_quality"
    mediaID = Column(String, ForeignKey("media.mediaID"), primary_key=True)
    quality_score = Column(Integer)
    noise_level = Column(DECIMAL(5, 2))

    media = relationship("Media", back_populates="sound_quality")