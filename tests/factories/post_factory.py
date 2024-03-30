import factory

from dw_blog_django.apps.blog.models import Post
from tests.factories.user_factory import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Faker("uuid4")
    episode_number = factory.Faker("random_int", min=1, max=100)
    title = factory.Sequence(lambda n: f"title_{n}")
    subtitle = factory.Sequence(lambda n: f"subtitle_{n}")
    slug = factory.Sequence(lambda n: f"slug_{n}")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("text")
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
