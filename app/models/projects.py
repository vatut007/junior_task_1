from sqlalchemy import Column, String, Integer, ForeignKey

from app.core.db import Base


class Projects(Base):
    code = Column(Integer, nullable=False)
    name = Column(String(length=100), unique=True, nullable=False)
    values = Column(Integer, ForeignKey('values.id'))
