from .base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String(20), nullable=True, unique=True)            # Код отделения (например: 09.02.07)
    description = Column(Text, nullable=True)                        # Описание отделения
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь с группами
    groups = relationship("Group", back_populates="department", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name})>"

    groups = relationship("Group", back_populates="department")