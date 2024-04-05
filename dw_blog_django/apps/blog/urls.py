from django.urls import path

from dw_blog_django.apps.blog.views import MainPostView, MainSeriesView

urlpatterns = [
    path("", MainPostView.as_view(), name="main"),
    path("series/main_series", MainSeriesView.as_view(), name="main_series"),
]
