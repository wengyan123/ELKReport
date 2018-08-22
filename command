# beat
celery -A watcher beat --loglevel=DEBUG

# worker
celery worker -A watcher --loglevel=Info