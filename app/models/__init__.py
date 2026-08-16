from .base import Base
from .attestation import *
from .employee import *
from .group import *
from .journal import *
from .order import *
from .schedule import *
from .student import *
from .subject import *
from .workload import *
from .department import *

# Экспортируем все модели для удобного импорта
__all__ = [
    "Base",
    "Group",
    "Student",
    "StudentStatus",
    "Employee",
    "Subject",
    "Grade",
    "Lesson",
    "Attestation",
    "Order",
    "Workload",
    "Department",
]