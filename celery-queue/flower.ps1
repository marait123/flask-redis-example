# CELERY_BROKER_URL: redis://redis:6379/0
# CELERY_RESULT_BACKEND: redis://redis:6379/0

$Env:CELERY_BROKER_URL = "redis://localhost:6379/0"
$Env:CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
celery flower -A tasks