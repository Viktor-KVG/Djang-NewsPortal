from django.urls import path

# Импортируем созданное нами представление
from .views import  NewsCreate, NewsUpdate, Appointment


urlpatterns = [

   path('create/', NewsCreate.as_view(), name='news_create'),
   path('appointment/', Appointment.as_view(), name='appointments'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    ]