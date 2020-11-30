import django_filters
from .models import Post


class PostSearch(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ('post_type', 'title', 'category', 'time_created', 'time_updated_last', 'location', 'start_time', 'end_time',
                  'equipment', 'content', )
