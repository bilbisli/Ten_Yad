# from django.test import TestCase
# from django.test import Client
#
# from django.urls import reverse
# from homepage.models import User, Post, Category
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
#
#
# from django.contrib.auth.models import User # Required to assign User as a borrower
#
#
# class PostInstancesByUserListModelTest(TestCase):
#     def __init__(self, methodName='runTest'):
#         super().__init__(methodName)
#         self.client = None
#
#     def setUp(self):
#         # Create two users
#         # test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK', email="bilbisli@gmail.com")
#         # test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD', email="ofirgls5588@gmail.com")
#         #
#         # test_user1.save()
#         # test_user2.save()
#         new_user = User.objects.create_user(username='bilbisli', password='tenyad123456', email="bilbisli@gmail.com")
#         test_user1 = User.objects.get(id=1)
#
#
#         # Create a post
#         test_category = Category.objects.create(name='Home reno')
#         test_post = Post.objects.create(
#             user=test_user1,
#             title='Help paint my house',
#             location='beer sheva',
#             content='help me paint my house please - music and beer provided! :)',
#         )
#
#         # Create category as a post-step
#         category_objects_for_post = Category.objects.all()[0]
#         test_post.category = category_objects_for_post
#         test_post.save()
#
#         # Create 30 BookInstance objects
#         # number_of_book_copies = 30
#         # for book_copy in range(number_of_book_copies):
#         #     return_date = timezone.localtime() + datetime.timedelta(days=book_copy%5)
#         #     the_borrower = test_user1 if book_copy % 2 else test_user2
#         #     status = 'm'
#         #     BookInstance.objects.create(
#         #         book=test_book,
#         #         imprint='Unlikely Imprint, 2016',
#         #         due_back=return_date,
#         #         borrower=the_borrower,
#         #         status=status,
#         #     )
#
#     def test_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse('login'))
#         self.assertRedirects(response, '/login/?next=/')
#
#     def test_logged_in_uses_correct_template(self):
#         c = Client()
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = c.post('/login/', {'username': 'testuser1', 'password': '1X'})
#
#         # Check our user is logged in
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         # Check that we got a response "success"
#         self.assertEqual(response.status_code, 200)
#
#         # Check we used correct template
#         self.assertTemplateUsed(response, 'homepage/homepage.html')
#
# #
# #
# # class ModelsTestCase(unittest.TestCase):
# #     def __init__(self, methodName='runTest'):
# #         super().__init__(methodName)
# #         self.client = None
# #         self.user = User.objects.create_user(username='testuser', password='ten12345', email="testing@gmail.com")
# #
# #     def setUp(self):
# #         # self.user = User.objects.create_user(username='testuser', password='ten12345', email="testing@gmail.com")
# #         # new_user = authenticate(username='testuser',
# #         #                         password='ten12345',
# #         #                         )
# #         # login = self.client.login(new_user)
# #         # user = self.user
# #
# #
# #         # user = User.objects.create_user('tester10', 'tester10@testing.com', 'testpass123456', )
# #         # user.save()
# #         # user.profile.phone = "0523357896"
# #         # user.profile.show_phone = True
# #         # user.profile.telegram = "tester"
# #         # user.profile.save()
# #
# #         post = Post(
# #             user=self.user,
# #             title="need help with homework",
# #             post_status="active",
# #             equipment="no equipment needed",
# #             content="help me with homework"
# #         )
# #         post.save()
# #         pass
# #
# #     def tearDown(self):
# #         user = User.objects.get(username="testuser")
# #         user.delete()
# #
# #     def test_user_fields(self):
# #         user = User.objects.get(username="testuser")
# #         self.assertTrue(user.profile.telegram == "testuser")
# #
# #     def test_post_fields(self):
# #         post = Post.objects.get(content="help me with homework")
# #         self.assertTrue(post.equipment == "need a car")
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
# #
# #
# # class MyTestCase(unittest.TestCase):
# #     def test_something(self):
# #         self.assertEqual(True, True)
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
