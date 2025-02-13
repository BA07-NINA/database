import datetime
from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

class Devices(Base):
    tablename = "devices"
    deviceID = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    info = Column(Text)
   
