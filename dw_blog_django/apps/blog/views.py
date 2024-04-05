from django.views.generic import ListView

from dw_blog_django.apps.blog.models import Post


class MainPostView(ListView):
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
        ).order_by("-episode_number")[:8]


class MainSeriesView(ListView):
    model = Post
    template_name = "blog/pages/main_series.html"
    content_object_name = "main_posts"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(series="main").order_by("-episode_number")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_posts"] = context["object_list"]
        return context
