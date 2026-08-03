from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import relationship
from app.models.base import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    position = Column(String(100))
    department = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    employment_date = Column(Date)

    workload = relationship("Workload", back_populates="employee")