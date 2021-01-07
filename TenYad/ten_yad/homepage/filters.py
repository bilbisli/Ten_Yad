import django_filters
from django import forms

from .models import Post, Category
from django_filters import CharFilter


class PostSearch(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('post_type', 'category', 'title', 'content', 'location')
        widgets = {
            'search': forms.TextInput(attrs={'class': 'search_posts'}),
        }


class VolunteerSearch(django_filters.FilterSet):
    category = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')