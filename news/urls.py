from django.urls import path

# Импортируем созданное нами представление
from .views import NewsCreate, NewsUpdate, CategoryListView, subscribe, NewsDetail, NewsSearch

urlpatterns = [
   path('<int:pk>', NewsDetail.as_view()),
   path('search/', NewsSearch.as_view(),name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe'),
    ]