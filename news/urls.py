from django.urls import path

# Импортируем созданное нами представление
from .views import NewsCreate, NewsUpdate, CategoryListView, subscribe, NewsDetail, NewsSearch
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('<int:pk>/', cache_page(60*5)(NewsDetail.as_view()), name='new'),
   path('search/', NewsSearch.as_view(),name='news_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', cache_page (100)(NewsUpdate.as_view()), name='news_update'),
   path('categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe')
   ]