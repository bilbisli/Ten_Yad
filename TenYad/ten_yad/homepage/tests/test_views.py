from django.test import TestCase
from homepage.models import User, Post, Profile, Category, Message
from homepage.views import get_icon, add_points, calculate_rating


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testerFinal2', 'tester@testing.com', 'testpassword')
        self.user.save()
        self.user.profile.phone = "05233578962"
        self.user.profile.show_phone = True
        self.user.profile.telegram = "tester2"
        self.user.profile.save()
        self.category = Category(name="sport2")
        self.category1 = Category(name="test_category")
        self.category.save()
        self.category1.save()

        self.post = Post(
            user=self.user,
            title="need help with homework1",
            content="help me with homework please1",
            category=self.category
        )
        self.post1 = Post(
            user=self.user,
            title="need help with homework1",
            content="help me with homework please1",
            category=self.category1
        )
        self.post2 = Post(
            user=self.user,
            title="need help with homework2",
            content="help me with homework please2",
            category=self.category1
        )
        self.post3 = Post(
            user=self.user,
            title="need help with homework3",
            content="help me with homework please3",
            category=self.category1
        )
        self.post.save()
        self.post1.save()
        self.post2.save()
        self.post3.save()
        pass

    def tearDown(self):
        user = User.objects.get(id=self.user.pk)
        user.delete()
        self.category.delete()
        self.category1.delete()

    def test_get_icon_by_alert(self):
        # tests functions: add_points, calculate_assists_categories, get_icon
        get_icon(user=self.user, category=self.category1)
        self.post1.users_assist.add(self.user)
        self.post1.save()
        self.assertFalse(self.user.profile.unread_notifications)
        get_icon(user=self.user, category=self.category1)
        self.post2.users_assist.add(self.user)
        self.post2.save()
        self.assertFalse(self.user.profile.unread_notifications)
        get_icon(user=self.user, category=self.category1)
        self.post.users_assist.add(self.user)
        self.post.save()
        self.assertFalse(self.user.profile.unread_notifications)
        get_icon(user=self.user, category=self.category1)
        self.post3.users_assist.add(self.user)
        self.post3.save()
        get_icon(user=self.user, category=self.category1)
        self.assertFalse(self.user.profile.unread_notifications)
        add_points(self.user, 51)
        get_icon(user=self.user, category=self.category1)
        self.user.profile.save()
        self.assertTrue(self.user.profile.unread_notifications)


    def test_calculate_rating(self):
        self.assertEqual(calculate_rating(self.user), 0)
        self.user.profile.rating_sum = 54
        self.user.profile.rating_count = 17
        self.assertEqual(calculate_rating(self.user), 3.2)
