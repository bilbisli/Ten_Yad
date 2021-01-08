from django.test import TestCase
from homepage.models import User, Post, Profile, Category, Message
from homepage.views import get_icon, add_points, calculate_rating


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testerFinal1', 'tester@testing.com', 'testpassword')
        self.user2 = User.objects.create_user('testerFinal2', 'tester@testing.com', 'testpassword')
        self.user.save()
        self.user.profile.phone = "05233578962"
        self.user.profile.show_phone = True
        self.user.profile.telegram = "tester2"
        self.user.profile.save()
        self.category = Category(name="sport2")
        self.category1 = Category(name="test_category")
        self.category.save()
        self.category1.save()
        self.posts = []
        for post_number in range(9):
            if post_number < 7:
                self.posts.append(
                    Post(
                        user=self.user2,
                        title=f"need help with homework {post_number}",
                        content=f"help me with homework please {post_number}",
                        category=self.category
                    )
                )
            else:
                self.posts.append(
                    Post(
                        user=self.user2,
                        title=f"need help with homework {post_number}",
                        content=f"help me with homework please {post_number}",
                    )
                )
            self.posts[post_number].save()

    def tearDown(self):
        user = User.objects.get(id=self.user.pk)
        user.delete()
        self.category.delete()
        self.category1.delete()

    def test_get_icon_by_alert_and_certificate(self):
        # tests functions: add_points, calculate_assists_categories, get_icon
        for post in self.posts[:3]:
            # adding assist in 3 posts of the same category and checking each time
            post.users_assist.add(self.user)
            get_icon(user=self.user, category=self.category)
            self.assertFalse(self.user.profile.unread_notifications)
        # adding assist in a post without a category and checking
        self.posts[8].users_assist.add(self.user)
        get_icon(user=self.user, category=self.category)
        self.assertFalse(self.user.profile.unread_notifications)
        # adding enough points to get the icon - user will get notified for getting an icon
        add_points(self.user, 50)
        get_icon(user=self.user, category=self.category)
        self.assertTrue(self.user.profile.unread_notifications)
        # adding enough points to get the second icon
        add_points(self.user, 50)
        for post in self.posts[3:5]:
            # adding assist in 2 more posts of the same category and checking each time
            post.users_assist.add(self.user)
            self.assertNotEqual(self.user.profile.unread_notifications, 2)
            get_icon(user=self.user, category=self.category)
        self.assertEqual(self.user.profile.unread_notifications, 2)
        for post in self.posts[5:8]:
            # adding assist in 2 more posts of the same category and checking each time
            post.users_assist.add(self.user)
            get_icon(user=self.user, category=self.category)
            self.assertNotEqual(self.user.profile.unread_notifications, 3)
        # adding not enough points to get the third icon
        add_points(self.user, 99)
        get_icon(user=self.user, category=self.category)
        self.assertNotEqual(self.user.profile.unread_notifications, 3)
        # adding enough points to get the third icon
        add_points(self.user, 1)
        get_icon(user=self.user, category=self.category)
        self.assertEqual(self.user.profile.unread_notifications, 3)
        # adding enough points for certificate eligibility - certificate is sent automatically
        add_points(self.user, 51)
        self.assertEqual(self.user.profile.unread_notifications, 4)

    def test_calculate_rating(self):
        self.assertEqual(calculate_rating(self.user), 0)
        self.user.profile.rating_sum = 54
        self.user.profile.rating_count = 17
        self.assertEqual(calculate_rating(self.user), 3.2)

