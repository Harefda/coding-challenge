from sqlalchemy import String, Integer
from sqlalchemy.sql.schema import Column
from app.db import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


