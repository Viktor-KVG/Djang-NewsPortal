from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import NewsForm
from .models import Post


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


from django.shortcuts import render

# Create your views here.
