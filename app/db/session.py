from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", "5432")
name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def enable_unaccent_extension():
    with SessionLocal() as db:
        try:
            db.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))
            db.commit()
            logging.info("Successfully enabled unaccent extension.")
        except Exception as e:
            db.rollback()
            logging.error(f"Error enabling unaccent extension: {e}")