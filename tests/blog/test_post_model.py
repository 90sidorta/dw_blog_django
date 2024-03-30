import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(title="post_title")
        assert post.__str__() == "post_title"

    def test_post_model(self, post_factory):
        post = post_factory(
            title="post_title",
            content="post_content",
            slug="post_slug",
            episode_number=1,
            published=True,
            approved=True,
            post_type="author",
            wykop_link="https://wykop.pl",
            podcast_link="https://podcast.com",
            series="main",
            notes="post_notes",
        )

        assert post.title == "post_title"
        assert post.content == "post_content"
        assert post.slug == "post_slug"
        assert post.episode_number == 1
        assert post.published
        assert post.approved
        assert post.post_type == "author"
        assert post.wykop_link == "https://wykop.pl"
        assert post.podcast_link == "https://podcast.com"
        assert post.series == "main"
        assert post.notes == "post_notes"
