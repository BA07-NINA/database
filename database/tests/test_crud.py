from src.db import SessionLocal
from src.crud import get_all_deployments

def test_get_all_deployments():
    db = SessionLocal()
    deployments = get_all_deployments(db)
    assert isinstance(deployments, list)

def test_get_media_by_id(db_session):
    media = get_media_by_id(db_session, "file1.mp3")
    assert media is not None
    assert media.file_path == "/path/to/file1.mp3"
