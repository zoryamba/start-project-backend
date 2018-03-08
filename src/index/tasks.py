from celery_app import celery_app


@celery_app.task
def add(x, y):
    return str(x + y)
