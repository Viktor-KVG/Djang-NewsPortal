import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('news.apps.NewsConfig')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'news.board.tasks.last_news',
        'schedule': crontab(minute='0', hour='8', day_of_week='mon'),
    },
}