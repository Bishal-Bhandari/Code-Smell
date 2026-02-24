# backend/celery_app/celery_app.py
from celery import Celery

# Create Celery instance
celery = Celery(
    "ai_code_reviewer",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Autodiscover tasks inside analysis_engine folder
# "analysis_engine.tasks" must be importable from this file
celery.autodiscover_tasks(["backend.analysis_engine.tasks"])