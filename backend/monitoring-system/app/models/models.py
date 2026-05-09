from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String)
    cpu = Column(Float)
    ram = Column(Float)
    status = Column(String)
    timestamp = Column(String)