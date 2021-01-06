import django_filters
from .models import Post, Category
from django_filters import CharFilter


class PostSearch(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('post_type', 'category', 'title', 'content', 'location')


class VolunteerSearch(django_filters.FilterSet):
    category = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')