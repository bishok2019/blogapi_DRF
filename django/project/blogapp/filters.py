import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'Created At'),
            ('title', 'Title'),
        )
    )

    class Meta:
        model = Post
        fields = ['ordering']