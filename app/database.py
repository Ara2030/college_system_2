from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.config import SQLALCHEMY_DATABASE_URL

# === Настройка подключения к базе данных ===
# Замени строку ниже на свои данные подключения
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/college_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Зависимость для FastAPI (используется в роутерах)
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()