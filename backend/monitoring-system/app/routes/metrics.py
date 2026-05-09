from fastapi import APIRouter, Depends

from app.database import SessionLocal
from app.models.models import Metric
from app.services.monitor_service import get_system_metrics
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.get("/metrics")
def metrics():

    data = get_system_metrics()

    db = SessionLocal()

    metric = Metric(
        server_name="Alpha",
        cpu=data["cpu"],
        ram=data["ram"],
        status=data["status"],
        timestamp=data["timestamp"]
    )

    db.add(metric)
    db.commit()

    return data


@router.get("/history")
def history():

    db = SessionLocal()

    metrics = db.query(Metric).all()

    return metrics