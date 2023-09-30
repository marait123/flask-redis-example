from flask import Flask, render_template
from celery import Celery
import os
from tasks import add  # Import your Celery task

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = os.environ.get(
    'CELERY_BROKER_URL', 'redis://redis:6379/0')
app.config['CELERY_RESULT_BACKEND'] = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://redis:6379/0')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
# check if celery is running
print(celery.control.inspect().active())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/<int:param1>/<int:param2>')
def add_route(param1, param2):
    result = add.delay(param1, param2)
    return result.id
    return str(result.get(timeout=3))

# get the result using id


@app.route('/result/<task_id>')
def get_result(task_id):
    result = add.AsyncResult(task_id)
    return str(result.get(timeout=3))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
