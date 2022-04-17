from sqlalchemy import String, Integer
from sqlalchemy.sql.schema import Column
from app.db import Base


class Test(Base):
    __tablename__ = "date"

    id = Column(Integer, primary_key=True)



