from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import students, groups, journal, schedule
from app.database import engine
from app.models import Base

# Создаём таблицы только если нужно (можно закомментировать при использовании Alembic)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Информационная система колледжа СПО",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)
app.include_router(groups.router)
app.include_router(journal.router)
app.include_router(schedule.router)


@app.get("/")
def root():
    return {"message": "ИС Колледжа работает"}