from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    name = 'appointments'

    # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    def ready(self):
        import appointments.signals

