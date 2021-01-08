from django.test import TestCase
from homepage.models import User, Profile
from homepage.forms import EditProfile, EditUser


class FormsTestsCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testerFinal', 'tester@testing.com', 'testpassword')
        self.user.save()
        self.user.profile.phone = "0523357896"
        self.user.profile.show_phone = True
        self.user.profile.telegram = "tester"
        self.user.profile.save()
        pass

    def tearDown(self):
        user = User.objects.get(id=self.user.pk)
        user.delete()

    def test_profile_edit(self):
        form1_data = {
            'phone': '044488775',
            'user': self.user,
            'telegram': 'tester 2',
            'show_telegram': True,
            'other_contact': 'none',
            'description': 'i like to help people',
        }
        form2_data = {
            'email': 'testing_change@email.com',
            'user': self.user
        }
        profile_form = EditProfile(data=form1_data, instance=self.user)
        user_form = EditUser(data=form2_data, instance=self.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

        self.assertEqual(self.user.email, 'testing_change@email.com')
        self.assertNotEqual(self.user.email, 'tester@testing.com')
