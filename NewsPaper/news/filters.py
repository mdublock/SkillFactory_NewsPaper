import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    categories = django_filters.CharFilter(lookup_expr='icontains')
    created_at__gte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte',
                                                    widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['title', 'categories', 'created_at__gte']