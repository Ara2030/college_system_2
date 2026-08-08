from __future__ import annotations
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Workload(Base):
    __tablename__ = "workloads"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="workloads")