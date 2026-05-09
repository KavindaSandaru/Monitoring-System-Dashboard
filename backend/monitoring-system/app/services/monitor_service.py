import psutil
from datetime import datetime


def get_system_metrics():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    if cpu >= 90:
        status = "CRITICAL"
    elif cpu >= 70:
        status = "WARNING"
    else:
        status = "HEALTHY"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "cpu": cpu,
        "ram": ram,
        "status": status,
        "timestamp": timestamp
    }