from fastapi import FastAPI
from app.routers import students, journal, schedule

app = FastAPI(title="ИС Колледжа СПО", version="1.0")

app.include_router(students.router)
app.include_router(journal.router)
app.include_router(schedule.router)

@app.get("/")
def root():
    return {"message": "Информационная система колледжа"}