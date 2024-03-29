from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    episode_number = models.IntegerField(editable=False, unique=False)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    post_type = models.CharField(
        max_length=20,
        default="author",
        choices=(
            ("author", "Author"),
            ("admin", "Admin"),
            ("translation", "Translation"),
        ),
    )
    wykop_link = models.URLField(blank=False, null=False)
    podcast_links = models.URLField(blank=True, null=True)
    series = models.CharField(
        max_length=200,
        default="main",
        choices=(
            ("main", "Main"),
            ("ancient_christianity", "Ancient Christianity"),
            ("islamic_history", "Islamic History"),
            ("orthodox_christainity", "Orthodox Christianity"),
            ("reformation", "Reformation"),
            ("non_european_christianity", "Non-European Christianity"),
        ),
    )

    class Meta:
        ordering = ("-episode_number",)

    def __str__(self):
        return self.title
