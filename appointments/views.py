from django.shortcuts import render
from .models import Appointment
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, reverse, redirect

class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(date=datetime.strptime(request.POST['date'], "%Y-%M-%d"),
                                  client_name=request.POST['client_name'],
                                  message=request.POST['message'],
                                  )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='Viteeek91.90@yandex.ru',
            # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=['vitass91.90@gmail.com']  # Здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        html_content = render_to_string('appointment_created.html', {'appointment': appointment, })

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,  # это то же, что и message
            from_email='Viteeek91.90@yandex.ru',
            to=['vitass91.90@gmail.com'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()
        return redirect('appointments')
# Create your views here.
