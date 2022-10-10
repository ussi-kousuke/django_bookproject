from cProfile import label
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
      class Meta:
            model = Book
            fields = ('title', 'category')
            labels = {
                'title': '対象書籍 :',
                'category': 'カテゴリ :'

            }
            widgets = {
                'title': forms.TextInput(attrs={'placeholder':'書籍のタイトルを入力'}),
            }


