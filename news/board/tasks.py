from celery import shared_task
import time
import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from NewsPortal import settings
from news.models import News,Category


@shared_task
def last_news():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = News.objects.filter(created_at__gte=last_week)
    categories = set(posts.values_list('category__name', Flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', Flat=True))
    html_content = render_to_string('daily_post.html', {'link': settings.SITE_URL, 'posts': posts, })

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
        )
    msg.attach_alternative(html_content, 'tex/html')
    msg.send()