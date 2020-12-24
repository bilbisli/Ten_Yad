import unittest
from .models import *

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user('tester', 'tester@testing.com', 'testpassword')
        user.save()
        user.profile.phone = "0523357896"
        user.profile.show_phone = True
        user.profile.telegram = "tester"
        user.profile.save()
        post = Post(
            user=user,
            title="need help with homework",
            post_status="active",
            equipment="no equipment needed",
            content="help me with homework"
        )
        post.save()
        pass

    def tearDown(self):
        user = User.objects.get(username="tester")
        user.delete()

    def test_user_fields(self):
        user = User.objects.get(username="tester")
        self.assertTrue(user.profile.telegram == "tester")

    def test_post_fields(self):
        post = Post.objects.get(content="help me with homework")
        self.assertTrue(post.equipment == "need a car")
