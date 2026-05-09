from pydantic import BaseModel


class MetricResponse(BaseModel):
    cpu: float
    ram: float
    status: str
    timestamp: str