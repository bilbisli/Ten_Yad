import unittest
from homepage.models import User, Post


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        user = User.objects.create_user('testerFinal', 'tester@testing.com', 'testpassword')
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
            content="help me with homework please"
        )
        post.save()
        pass

    def tearDown(self):
        user = User.objects.get(username="testerFinal")
        user.delete()

    def test_user_fields(self):
        user = User.objects.get(username="testerFinal")
        self.assertTrue(user.profile.telegram == "tester")

    def test_post_fields(self):
        post = Post.objects.get(content="help me with homework please")
        self.assertTrue(post.equipment == "no equipment needed")


def main():
    ModelsTestCase


if __name__ == '__main__':
    unittest.main()



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
