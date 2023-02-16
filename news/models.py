from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rating_articles_author = Post.objects.filter(author_id = self.pk).aggregate(sum_articles = Sum('rate_news'))['rate_news']
        rating_comment_author = Comment.objects.filter(users_id=self.users).aggregate(sum_articles=Sum('rate_comment'))['rate_comment']
        rating_comment_posts = Comment.objects.filter(post__author__users=self.users).aggregate(sum_posts=Sum('rate_comment'))['rate_comment']
        self.rating = rating_articles_author*3 + rating_comment_author + rating_comment_posts
        self.save()


class Category(models.Model):

    policy = 'PO'
    news = 'NE'
    education = 'ED'
    article = 'AR'

    TYPES_CATEGORY = [
        (policy, 'Политика'),
        (news, 'Новости'),
        (education, 'Образование'),
        (article,'Статья')
    ]

    type_positions = models.CharField(max_length=2, choices=TYPES_CATEGORY, default=policy, unique = True)

class Post(models.Model):

    news = 'NEW'
    article = 'ART'

    TYPES = [
        (news, 'Новости'),
        (article, 'Статья')
    ]

    post_author = models.ForeignKey('Author', on_delete=models.CASCADE)
    choice_category = models.CharField(max_length=3, choices=TYPES, default=news)
    time_in = models.DateTimeField(auto_now_add=True)
    link = models.ManyToManyField(Category, through='PostCategory')
    title_news = models.CharField(max_length=255, blank=False)
    text_news = models.TextField(blank=False)
    rate_news = models.IntegerField(default=0)

    def prewiev(self):
        dots = self.text_news
        return dots[0:124] + '...'

    def like(self):
        self.rate_news += 1
        self.save()


    def dislike(self):
        self.rate_news -= 1
        self.save()

class PostCategory(models.Model):

    link_1 = models.ForeignKey('Post', on_delete=models.CASCADE)
    link_2 = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    link_3 = models.ForeignKey(Post, on_delete=models.CASCADE)
    link_4 = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(blank = False)
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rate_comment = models.IntegerField(default=1)


    def like(self):
        self.rate_comment += 1
        self.save()

    def dislike(self):
        self.rate_comment -= 1
        self.save()