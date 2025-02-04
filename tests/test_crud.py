from src.db import SessionLocal
from src.crud import get_all_deployments

def test_get_all_deployments():
    db = SessionLocal()
    deployments = get_all_deployments(db)
    assert isinstance(deployments, list)
