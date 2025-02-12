import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://your_user:your_password@localhost/nina_database")