import unittest
from django.test import TestCase, Client
from django.urls import reverse
from homepage.models import User, Post, Profile, Category, Message
from homepage.views import send_alert


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testerFinal', 'tester@testing.com', 'testpassword')
        self.user.save()
        self.user.profile.phone = "0523357896"
        self.user.profile.show_phone = True
        self.user.profile.telegram = "tester"
        self.user.profile.save()
        self.category = Category(name="sport")
        self.category.save()
        self.post = Post(
            user=self.user,
            title="need help with homework",
            post_status="active",
            equipment="no equipment needed",
            content="help me with homework please"
        )
        self.post.category = self.category
        self.post.save()
        pass

    def tearDown(self):
        user = User.objects.get(id=self.user.pk)
        user.delete()
        self.category.delete()

    def test_user_fields(self):
        user = User.objects.get(id=self.user.pk)
        self.assertTrue(user.profile.telegram == "tester")
        self.assertFalse(user.profile.telegram == "tester1")

    def test_profile_fields(self):
        user = User.objects.get(id=self.user.pk)
        profile = self.user.profile
        self.assertEqual(str(profile), 'testerFinal')
        self.assertEqual(user.email, 'tester@testing.com')
        user.profile.set_email('other@email.com')
        self.assertEqual(user.profile.get_email(), 'other@email.com')
        self.assertNotEqual(user.email, 'tester@testing.com')

    def test_post_fields(self):
        post = Post.objects.get(id=self.post.pk)
        self.assertTrue(post.equipment == "no equipment needed")
        self.assertEqual(post.post_status, (Post.PostStatus.ACTIVE).lower())
        self.assertEqual(str(self.post), f'title: need help with homework, author: testerFinal, category: sport')

    def test_logged_in_user_model(self):
        c = Client()
        login = self.client.login(username='testerFinal', password='testpassword')
        response = c.post('/login/', {'username': 'testerFinal', 'password': 'testpassword'})

        # check that we got a response "success"
        self.assertEqual(response.status_code, 302)

        # check change password success with login
        self.user.profile.set_password("newpass123")
        response = c.post('/login/', {'username': 'testerFinal', 'password': 'testpassword'})
        self.assertNotEqual(response.status_code, 302)

    def test_category_in_post(self):
        self.post.category = self.category
        self.assertEqual(str(self.post.category), str(self.category))

    def test_message_to_user_with_alert(self):
        self.assertEqual(self.user.profile.unread_notifications, 0)
        send_alert(user=self.user, message="test notification")
        self.assertEqual(self.user.profile.unread_notifications, 1)
        self.message = Message.objects.all().first()
        self.assertEqual(self.message.notification, "test notification")
        self.assertNotEqual(self.message.notification, "test notificationn")
        self.assertEqual(str(self.message), f'test notification, {self.user.profile}, time: {self.message.time}')
