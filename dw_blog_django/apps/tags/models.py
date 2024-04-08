from django.db import models

from dw_blog_django.apps.blog.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    posts = models.ManyToManyField(Post, related_name="tags", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        if self.description:
            self.description = self.description.strip()
        if not self.name.startswith("#"):
            self.name = "#" + self.name
        super().save(*args, **kwargs)
