from pydantic import BaseModel
from typing import Optional, List

class DeploymentBase(BaseModel):
    deploymentID: str
    deviceID: str
    latitude: float
    longitude: float
    date_start: str
    date_end: Optional[str]
    notes: Optional[str]

class Deployment(DeploymentBase):
    class Config:
        orm_mode = True
