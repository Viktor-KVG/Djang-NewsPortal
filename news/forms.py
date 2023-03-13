from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'post_author',
           'title_news',
           'text_news',
           'choice_category',
       ]

   def clean(self):
       cleaned_data = super().clean()
       name = cleaned_data.get("post_author")
       description = cleaned_data.get("choice_category")

       if name == description:
           raise ValidationError("Заголовок не должент быть идентичен категории.")

       return cleaned_data