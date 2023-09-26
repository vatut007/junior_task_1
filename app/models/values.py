from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class Values(Base):
    plan = Column(Integer, nullable=False)
    fact = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    project = relationship('Projects', cascade='delete')
