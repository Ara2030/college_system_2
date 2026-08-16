from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models.base import Base          # ← Берём Base из models/base.py

# === Важно: импортируем все модели ===
from .models import *

from app.routers import (
    students, groups, journal, schedule, 
    employees, subjects, attestation, orders
)

app = FastAPI(title="Информационная система колледжа СПО", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Подключение роутеров
app.include_router(students.router)
app.include_router(groups.router)
app.include_router(journal.router)
app.include_router(schedule.router)
app.include_router(employees.router)
app.include_router(subjects.router)
app.include_router(attestation.router)
app.include_router(orders.router)

# Статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "ИС Колледжа работает"}


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"status": "Подключение к базе работает"}