from typing import Generator

from sqlalchemy.orm import Session

from core.logger import get_logger
from database.connection import DatabaseBase, SessionLocal, engine

logger = get_logger(__name__)


def initialize_database():
    logger.info("INITIALIZING DATABASE")

    # Import models so SQLAlchemy registers them
    from database.models import Appointment, CalendarSyncJob

    DatabaseBase.metadata.create_all(bind=engine)

    logger.info("DATABASE INITIALIZED")


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()