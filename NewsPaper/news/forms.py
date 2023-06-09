from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author',
        ]
