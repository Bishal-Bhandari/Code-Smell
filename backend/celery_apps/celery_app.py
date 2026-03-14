# backend/celery_app/celery_app.py
from celery import Celery
from celery.schedules import crontab

# Create Celery instance
celery = Celery(
    "ai_code_reviewer",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Autodiscover tasks inside analysis_engine folder
celery.autodiscover_tasks(["backend.analysis_engine.tasks"])

#resets montly usages count on 1st of month
celery.conf.beat_schedule = {
    "reset-usage-monthly": {
        "task": "analysis_engine.tasks.reset_monthly_usage",
        "schedule": crontab(day_of_month=1, hour=0, minute=0),
    }
}