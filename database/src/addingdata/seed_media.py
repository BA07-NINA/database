import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

import os
from datetime import datetime
from sqlalchemy.orm import Session
from db import engine
from models import Media, Deployment

# Define the directory containing the media files
media_dir = "../exampledata/conf_20240314_TABMON"
print(f"Media directory: {media_dir}")

# Default deployment ID for this seeding (ensure this exists in the database)
DEFAULT_DEPLOYMENT_ID = "DEP1"  # Replace with an actual deployment ID from your database

# Function to seed media data
def seed_media_data():
    session = Session(bind=engine)
    try:
        # Check if the default deployment exists
        deployment = session.query(Deployment).filter(Deployment.deploymentID == DEFAULT_DEPLOYMENT_ID).first()
        if not deployment:
            raise ValueError(f"Deployment with ID '{DEFAULT_DEPLOYMENT_ID}' does not exist in the database.")

        # Loop through each file in the directory
        for file_name in os.listdir(media_dir):
            file_path = os.path.join(media_dir, file_name)

            # Skip non-MP3 files
            if not file_name.endswith(".mp3"):
                continue

            # Check if the media already exists in the database
            if session.query(Media).filter(Media.mediaID == file_name).first():
                print(f"Media '{file_name}' already exists. Skipping...")
                continue

            # Get file metadata
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
            created_at = datetime.fromtimestamp(os.path.getctime(file_path))  # File creation time

            # Insert the data into the database
            media = Media(
                mediaID=file_name,
                deploymentID=DEFAULT_DEPLOYMENT_ID,  # Link to the default deployment
                configuration=None,  # No configuration available for now
                timestamp=created_at,
                file_path=file_path,
                size_MB=round(file_size_mb, 2)
            )
            session.add(media)

        # Commit the transaction
        session.commit()
        print("Media data seeded successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding media data: {e}")
    finally:
        session.close()

# Run the seeding script
if __name__ == "__main__":
    seed_media_data()
