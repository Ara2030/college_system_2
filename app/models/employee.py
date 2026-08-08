from __future__ import annotations

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.models.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    position = Column(String)
    department = Column(String)
    phone = Column(String)
    email = Column(String)
    employment_date = Column(Date)

    # Исправленная связь
    workloads = relationship("Workload", back_populates="employee")