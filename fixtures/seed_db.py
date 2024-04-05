import os
import random

import django
import factory
from factory.faker import faker

FAKE = faker.Faker()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dw_blog_django.settings.development")
django.setup()

from django.contrib.auth.models import User

from dw_blog_django.apps.blog.models import Post


class FixturePostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Faker("uuid4")
    episode_number = factory.Faker("random_int", min=1, max=1000)
    title = factory.Faker("sentence", nb_words=5)
    subtitle = factory.Faker("sentence", nb_words=15)
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="andrzej")[0]
    published = factory.Faker("boolean")
    approved = factory.Faker("boolean")
    post_type = factory.Faker(
        "random_element", elements=["author", "admin", "translation"]
    )
    wykop_link = factory.Faker("url")
    podcast_link = factory.Faker("url")
    series = factory.Faker(
        "random_element",
        elements=[
            "main",
            "ancient_christianity",
            "islamic_history",
            "orthodox_christainity",
            "reformation",
            "non_european_christianity",
        ],
    )
    notes = factory.Faker("text")

    @factory.lazy_attribute
    def content(self):
        text_content = ""
        for _ in range(5, 10):
            text_content += (
                "\n" + FAKE.paragraph(nb_sentences=random.randint(15, 30)) + "\n"
            )
        return text_content


FixturePostFactory.create_batch(10)
