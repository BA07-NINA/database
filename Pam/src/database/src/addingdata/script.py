from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Deployment, Media, Observation, Device, SoundQuality, Annotation, User
import os

# Database connection URL
DATABASE_URL = os.environ("DATABASE_URL") #"postgresql+psycopg2://noah:noah@localhost:5432/database"  # Replace with your database URL

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Create tables
Base.metadata.create_all(engine)

def populate_data():
    try:
        # Step 1: Add devices (check for duplicates)
        existing_devices = {device.deviceID for device in session.query(Device).all()}
        devices = [
            Device(deviceID=f"D{i}", device_name=f"Sensor {chr(65+i)}", info=f"Sensor info {i}")
            for i in range(1, 6)
            if f"D{i}" not in existing_devices
        ]
        if devices:
            session.add_all(devices)
            session.commit()

        # Step 2: Add deployments
        existing_deployments = {deployment.deploymentID for deployment in session.query(Deployment).all()}
        deployments = [
            Deployment(
                deploymentID=f"DEP{i}",
                deviceID=f"D{i % 5 + 1}",
                latitude=59.0 + i * 0.1,
                longitude=10.0 + i * 0.1,
                date_start=datetime(2023, 1, 1) + timedelta(days=i),
                date_end=datetime(2023, 1, 10) + timedelta(days=i),
                notes=f"Deployment notes {i}",
            )
            for i in range(1, 11)
            if f"DEP{i}" not in existing_deployments
        ]
        if deployments:
            session.add_all(deployments)
            session.commit()

        # Step 3: Add media
        existing_media = {media.mediaID for media in session.query(Media).all()}
        media_files = [
            Media(
                mediaID=f"M{i}",
                deploymentID=f"DEP{i % 10 + 1}",
                configuration=f"Config {i}",
                timestamp=datetime(2023, 1, 1, 9, 0) + timedelta(hours=i),
                file_path=f"/media/file_{i}.wav",
                size_MB=15.0 + i * 0.5,
            )
            for i in range(1, 21)
            if f"M{i}" not in existing_media
        ]
        if media_files:
            session.add_all(media_files)
            session.commit()

        # Step 4: Add observations
        existing_observations = {obs.eventID for obs in session.query(Observation).all()}
        observations = [
            Observation(
                eventID=f"E{i}",
                mediaID=f"M{i % 20 + 1}",
                info=f"Observation info {i}",
                time_start=datetime(2023, 1, 1, 9, 0) + timedelta(hours=i),
                time_end=datetime(2023, 1, 1, 9, 30) + timedelta(hours=i),
            )
            for i in range(1, 31)
            if f"E{i}" not in existing_observations
        ]
        if observations:
            session.add_all(observations)
            session.commit()

        # Step 5: Add sound quality
        existing_sound_quality = {sq.mediaID for sq in session.query(SoundQuality).all()}
        sound_quality_records = [
            SoundQuality(
                mediaID=f"M{i % 20 + 1}",
                quality_score=80 + i % 10,
                noise_level=10.0 + i * 0.1,
            )
            for i in range(1, 21)
            if f"M{i % 20 + 1}" not in existing_sound_quality
        ]
        if sound_quality_records:
            session.add_all(sound_quality_records)
            session.commit()

        # Step 6: Add annotations
        existing_annotations = {annotation.annotationID for annotation in session.query(Annotation).all()}
        annotations = [
            Annotation(
                annotationID=f"A{i}",
                mediaID=f"M{i % 20 + 1}",
                annotation_type="Type A" if i % 2 == 0 else "Type B",
                text=f"Annotation text {i}",
                timestamp=datetime(2023, 1, 1, 10, 0) + timedelta(hours=i),
            )
            for i in range(1, 41)
            if f"A{i}" not in existing_annotations
        ]
        if annotations:
            session.add_all(annotations)
            session.commit()

        # Step 7: Add users
        existing_users = {user.userID for user in session.query(User).all()}
        users = [
            User(
                userID=f"U{i}",
                username=f"user{i}",
                email=f"user{i}@example.com",
                password_hash=f"hashed_password_{i}",
                role="admin" if i % 2 == 0 else "researcher",
            )
            for i in range(1, 11)
            if f"U{i}" not in existing_users
        ]
        if users:
            session.add_all(users)
            session.commit()

        print("All data successfully added!")

    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        session.close()

# Run the script
if __name__ == "__main__":
    populate_data()
