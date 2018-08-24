# beat
celery -A watcher beat --loglevel=INFO

# worker
celery worker -A watcher --loglevel=INFO