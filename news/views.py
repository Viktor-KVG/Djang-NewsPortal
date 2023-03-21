from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from .forms import NewsForm
from .models import Post, Category, News
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

#from .models import Appointment
class NewsCategory(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    ordering = '-name'
    # queryset = Product.objects.order_by('name')
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_words'] = 'Новостей нет'
        return context



class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'

class NewsSearch(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_search.html'

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

class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'] )
        queryset = Post.objects.filter(Category=self.category).order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message} )





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
