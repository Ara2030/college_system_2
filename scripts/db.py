# scripts/db.py
import sys
from alembic.config import main as alembic_main


def revision():
    """Создать новую миграцию"""
    sys.argv = ["alembic", "revision", "--autogenerate", "-m", " ".join(sys.argv[1:])]
    alembic_main()


def upgrade():
    """Применить миграции"""
    sys.argv = ["alembic", "upgrade", "head"]
    alembic_main()


def downgrade():
    """Откатить последнюю миграцию"""
    sys.argv = ["alembic", "downgrade", "-1"]
    alembic_main()


def history():
    """Показать историю миграций"""
    sys.argv = ["alembic", "history"]
    alembic_main()