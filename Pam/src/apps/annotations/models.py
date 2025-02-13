from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

class Annotation(Base):
    __tablename__ = "annotation"
    annotationID = Column(String, primary_key=True)
    mediaID = Column(String, ForeignKey("media.mediaID"), nullable=False)
    annotation_type = Column(String(50))
    text = Column(Text)
    timestamp = Column(TIMESTAMP)

    media = relationship("Media", back_populates="annotations")
    user = relationship("User", back_populates="annotations")