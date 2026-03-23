import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://", 1)

DEBUG = os.getenv("DEBUG", "False") == "True"

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não encontrado. Verifique o arquivo .env")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=DEBUG,
    future = True,
    connect_args={"sslmode": "require"} if "postgresql" in DATABASE_URL else{}
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()