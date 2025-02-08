import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../src")


import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Deployment, Media, User
from src.crud import (
    create_deployment,
    get_deployment_by_id,
    get_all_deployments,
    create_user,
    get_user_by_id,
    get_user_by_username,
)

# Create a test SQLite database
TEST_DATABASE_URL = "sqlite:///:memory:"

# Setup test engine and session
engine = create_engine(TEST_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Database fixture
@pytest.fixture(scope="function")
def db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session  # Provide the session to the test
    session.close()
    # Drop tables after test
    Base.metadata.drop_all(bind=engine)


# ------------------- Deployment Tests -------------------
def test_create_deployment(db):
    deployment = Deployment(
        deploymentID="DEP1",
        deviceID="DEV1",
        latitude=59.0,
        longitude=10.0,
        date_start="2023-01-01 10:00:00",
        notes="Sample deployment",
    )
    result = create_deployment(db, deployment)
    assert result.deploymentID == "DEP1"


def test_get_deployment_by_id(db):
    deployment = Deployment(
        deploymentID="DEP1",
        deviceID="DEV1",
        latitude=59.0,
        longitude=10.0,
        date_start="2023-01-01 10:00:00",
        notes="Sample deployment",
    )
    create_deployment(db, deployment)
    result = get_deployment_by_id(db, "DEP1")
    assert result is not None
    assert result.deploymentID == "DEP1"


def test_get_all_deployments(db):
    deployment1 = Deployment(
        deploymentID="DEP1",
        deviceID="DEV1",
        latitude=59.0,
        longitude=10.0,
        date_start="2023-01-01 10:00:00",
        notes="Sample deployment",
    )
    deployment2 = Deployment(
        deploymentID="DEP2",
        deviceID="DEV2",
        latitude=60.0,
        longitude=11.0,
        date_start="2023-01-02 10:00:00",
        notes="Another deployment",
    )
    create_deployment(db, deployment1)
    create_deployment(db, deployment2)
    result = get_all_deployments(db)
    assert len(result) == 2


# ------------------- User Tests -------------------
def test_create_user(db):
    user = User(
        userID="USER1",
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
        role="admin",
    )
    result = create_user(db, user)
    assert result.userID == "USER1"


def test_get_user_by_id(db):
    user = User(
        userID="USER1",
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
        role="admin",
    )
    create_user(db, user)
    result = get_user_by_id(db, "USER1")
    assert result is not None
    assert result.userID == "USER1"


def test_get_user_by_username(db):
    user = User(
        userID="USER1",
        username="testuser",
        email="test@example.com",
        password_hash="hashedpassword",
        role="admin",
    )
    create_user(db, user)
    result = get_user_by_username(db, "testuser")
    assert result is not None
    assert result.username == "testuser"

