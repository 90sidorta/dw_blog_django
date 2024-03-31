from django.urls import path

from dw_blog_django.apps.blog.views import MainView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
]
