from celery import Celery


app = Celery('Watcher')
app.config_from_object('celeryconfig')


@app.task
def test(arg):
    print(arg)


@app.task
def add(x, y):
    return x + y