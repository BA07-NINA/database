import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://your_user:your_password@localhost/nina_database")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
