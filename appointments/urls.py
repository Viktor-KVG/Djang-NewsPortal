from django.urls import path

# Импортируем созданное нами представление
from .views import AppointmentView


urlpatterns = [


   path('appointment/', AppointmentView.as_view(), name='appointments')
]