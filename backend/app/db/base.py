"""Declarative SQLAlchemy Base that every model in app/models inherits from.

Belongs to: Module 1 Data Intake.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
