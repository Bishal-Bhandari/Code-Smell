from celery import Celery
import app.tasks

# Celery instance
celery = Celery(
    "worker",
    # redis url
    broker="redis://localhost:6379/0",
    # opt result storage
    backend="redis://localhost:6379/0"
)

celery.autodiscover_tasks(["app.tasks"])