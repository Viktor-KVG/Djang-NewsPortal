from django.urls import path

# Импортируем созданное нами представление
from .views import NewsCreate, NewsUpdate, CategoryListView, subscribe


urlpatterns = [

   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('categories/<int:pk>', CategoryListView, name = 'category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe'),
    ]