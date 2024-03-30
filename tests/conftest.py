from pytest_factoryboy import register

from tests.factories.post_factory import PostFactory
from tests.factories.user_factory import UserFactory

register(UserFactory)
register(PostFactory)
