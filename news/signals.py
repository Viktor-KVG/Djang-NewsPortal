from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from NewsPortal import settings
from NewsPortal.settings import SITE_URL
from news.models import PostCategory
from news.views import subscribe


def send_notification(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
          'text': preview,
          'link': f'{SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject = 'title',
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = subscribers,
    )
    msg.attach.alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender = PostCategory)
def notify_aboute_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notification(instance.preview(), instance.pk(),instance.title, subscribers )



