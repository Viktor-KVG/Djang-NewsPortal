from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.shortcuts import render
from django.db.models.signals import m2m_changed
from news.models import Category, PostCategory, Post
from news.signals import send_notification
from django.template.loader import render_to_string
from NewsPortal import settings
from NewsPortal.settings import SITE_URL




@receiver(m2m_changed, sender = PostCategory)
def notify_about_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribers.all()

        subscribers_emails += [s.email for s in subscribers]

        send_notification(post.preview(), post.pk(),post.title, subscribers_emails)