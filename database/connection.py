from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.configs import settings


engine = create_engine(
    settings.DATABASE_URI,
    echo=False,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

DatabaseBase = declarative_base()