import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Correct connection string
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://noah:noah@localhost:5432/database")


# Engine
engine = create_engine(DATABASE_URL)

# Session factory
Session = sessionmaker(bind=engine)

def get_db():
    """Dependency function for database sessions"""
    db = Session()
    try:
        yield db
    finally:
        db.close()

