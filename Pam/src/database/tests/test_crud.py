import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../src")

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Deployment, Media, User, Device  # Ensure Device is imported
from src.crud import (
    create_deployment,
    get_deployment_by_id,
    get_all_deployments,
    create_user,
    get_user_by_id,
    get_user_by_username,
)

# Create a test psql database
TEST_DATABASE_URL = "postgresql+psycopg2://noahsyrdal:noah@localhost:5432/test_db"

# Setup test engine and session
engine = create_engine(TEST_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Database fixture
@pytest.fixture(scope="function")
def db():
    """ Creates a new database session for a test, then cleans up after. """
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        yield session  # Provide the session to the test
        session.commit()  # Ensure transactions are committed
    except Exception:
        session.rollback()  # Rollback on error
    finally:
        session.close()  # Close the session
        Base.metadata.drop_all(bind=engine)  # Cleanup database tables


# ------------------- Deployment Tests -------------------
def test_create_deployment(db):
    # Create a Device first to satisfy ForeignKey constraint
    device = Device(deviceID="DEV1", device_name="Test Device", info="Sample info")
    db.add(device)
    db.commit()  # Commit so that it's available before Deployment insert

    # Now create a Deployment
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
    # Ensure a Device exists first
    device = Device(deviceID="DEV1", device_name="Test Device", info="Sample info")
    db.add(device)
    db.commit()

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
    # Create devices first
    device1 = Device(deviceID="DEV1", device_name="Device 1", info="Info 1")
    device2 = Device(deviceID="DEV2", device_name="Device 2", info="Info 2")
    db.add_all([device1, device2])
    db.commit()

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


