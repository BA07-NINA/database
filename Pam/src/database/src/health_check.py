from sqlalchemy.exc import OperationalError
from db import engine

def check_database_health():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        print("Database is healthy!")
    except OperationalError:
        print("Database is unreachable!")
