from django.views.generic import ListView

from dw_blog_django.apps.blog.models import Post


class MainView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            episode_number__in=[
                51,
                66,
                67,
                75,
                82,
                83,
                86,
                91,
            ]
        ).order_by("-episode_number")[:10]
