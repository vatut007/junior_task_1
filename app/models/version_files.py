from sqlalchemy import Column, String, DateTime

from app.core.db import Base


class VersionFile(Base):
    name = Column(String(100), unique=True, nullable=False)
    date = Column(DateTime, nullable=False)
    projects = Column