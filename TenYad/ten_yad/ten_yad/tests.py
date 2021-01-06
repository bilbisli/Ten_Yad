# import unittest
# from django.test import TestCase, Client
# from django.urls import reverse
# from homepage.models import User, Post
#
#
# class ModelsTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('testerFinal', 'tester@testing.com', 'testpassword')
#         self.user.save()
#         self.user.profile.phone = "0523357896"
#         self.user.profile.show_phone = True
#         self.user.profile.telegram = "tester"
#         self.user.profile.save()
#         self.post = Post(
#             user=self.user,
#             title="need help with homework",
#             post_status="active",
#             equipment="no equipment needed",
#             content="help me with homework please"
#         )
#         self.post.save()
#         pass
#
#     def tearDown(self):
#         user = User.objects.get(username="testerFinal")
#         user.delete()
#
#     def test_user_fields(self):
#         user = User.objects.get(username="testerFinal")
#         self.assertTrue(user.profile.telegram == "tester")
#
#     def test_post_fields(self):
#         post = Post.objects.get(content="help me with homework please")
#         self.assertTrue(post.equipment == "no equipment needed")
#
#
#     # def test_redirect_if_not_logged_in(self):
#     #     response = self.client.get(reverse('login'))
#     #     self.assertRedirects(response, '/login/?next=/')
#
#     def test_logged_in_uses_correct_template(self):
#         c = Client()
#         login = self.client.login(username='testerFinal', password='testpassword')
#         response = c.post('/login/', {'username': 'testerFinal', 'password': 'testpassword'})
#
#         # Check our user is logged in
#         self.assertEqual(str(self.user.profile), 'testerFinal')
#         # Check that we got a response "success"
#         self.assertEqual(response.status_code, 302)
#
#         # Check we used correct template
#         # self.assertTemplateUsed(response, 'homepage/homepage.html')
