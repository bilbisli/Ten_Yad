import django_filters
from .models import Post
from django_filters import DateFilter, CharFilter


class PostSearch(django_filters.FilterSet):
    # start_date = DateFilter(field_name="start_time", lookup_expr='gte')
    # end_date = DateFilter(field_name="start_time", lookup_expr='lte')
    title = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('post_type', 'category', 'title', 'content', 'location')


#   ('post_type', 'title', 'category', 'location', 'start_time', 'end_time',
#   'equipment', 'content', )
