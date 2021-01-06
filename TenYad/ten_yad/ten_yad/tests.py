# from django.test import TestCase
#
# from django.contrib.auth.models import User
#
#
# class SignInViewTest(TestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user(username='test_ten_yad',
#                                                          password='test_ten_yad123',
#                                                          email='test10yad@example.com')
#
#     def tearDown(self):
#         self.user.delete()
#
#     def test_correct(self):
#         response = self.client.post('/login/', {'username': 'test_ten_yad', 'password': 'test_ten_yad123'})
#         self.assertTrue(response.data['authenticated'])
#
#     def test_wrong_username(self):
#         response = self.client.post('/login/', {'username': 'wrong', 'password': 'test_ten_yad123'})
#         self.assertFalse(response.data['authenticated'])
#
#     def test_wrong_pssword(self):
#         response = self.client.post('/login/', {'username': 'test_ten_yad', 'password': 'wrong'})
#         self.assertFalse(response.data['authenticated'])
