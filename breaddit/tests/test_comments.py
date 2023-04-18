from django.contrib.auth.models import User
from django.test import TestCase

from breaddit.models import Post, Comment


class CommentTestCase(TestCase):

    def test_get_returns_comments(self):

        user_1 = User.objects.create(
            username="testuser",
            email="foo@bar.com",
            first_name="Morty",
            last_name="Smith",
            is_active=True)

        user_2 = User.objects.create(
            username="testuser2",
            email="bar@foo.com",
            first_name="Rick",
            last_name="Sanchez",
            is_active=True)

        post = Post.objects.create(
            title="Test Post",
            body="This is a test post",
            author=user_1)

        comment_1 = Comment.objects.create(
            post=post,
            body="This is a test comment",
            author=user_1)

        comment_2 = Comment.objects.create(
            post=post,
            body="This is another test comment",
            author=user_2)

        response = self.client.get(f'/posts/{post.id}/comments/')
        self.assertEqual(response.status_code, 200)

    def test_get_returns_no_comments(self):

        user_1 = User.objects.create(
            username="testuser",
            email="foo@bar.com",
            first_name="Morty",
            last_name="Smith",
            is_active=True)

        user_2 = User.objects.create(
            username="testuser2",
            email="bar@foo.com",
            first_name="Rick",
            last_name="Sanchez",
            is_active=True)

        post = Post.objects.create(
            title="Test Post",
            body="This is a test post",
            author=user_1)

        response = self.client.get(f'/posts/{post.id}/comments/')
        self.assertEqual(response.status_code, 200)
