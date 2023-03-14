from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import NewsForm
from .models import Post
from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

#from .models import Appointment

class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.quantity = 13
        return super().form_valid(form)
class NewsUpdate(UpdateView):

    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


#class AppointmentView(View):
    #def get(self, request, *args, **kwargs):
     #   return render(request, 'make_appointment.html', {})

    #def post(self, request, *args, **kwargs):
     #   appointment = Appointment(date=datetime.strptime(request.POST['date'],"%Y-%M-%d"),
      #      client_name=request.POST['client_name'],
      #      message=request.POST['message'],
      #  )
      #  appointment.save()

      #  send_mail(
        #    subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
       #     # имя клиента и дата записи будут в теме для удобства
       #     message=appointment.message,  # сообщение с кратким описанием проблемы
       #     from_email='Viteeek91.90@yandex.ru',
            # здесь указываете почту, с которой будете отправлять (об этом попозже)
        #    recipient_list=['vitass91.90@gmail.com']  # здесь список получателей. Например, секретарь, сам врач и т. д.
       # )

      #  html_content = render_to_string('appointment_created.html',{'appointment': appointment,})

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
       # msg = EmailMultiAlternatives(
       #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
       #     body=appointment.message,  # это то же, что и message
       #     from_email='Viteeek91.90@yandex.ru',
       #     to=['vitass91.90@gmail.com'],  # это то же, что и recipients_list
       # )
       # msg.attach_alternative(html_content, "text/html")  # добавляем html

       # msg.send()
       # return redirect('appointments')



# Create your views here.
