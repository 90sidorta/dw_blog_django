from django.views.generic import ListView

from dw_blog_django.apps.blog.models import Post


class MainView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
