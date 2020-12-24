from django import forms
from .models import Post, Profile, User

class AssistOfferForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'post_type',
            'location',
            'start_time',
            'end_time',
            'content',
            'equipment',
        ]
        exclude = ['user']
# class EditProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = [
#             'gender',
#             'birth_date',
#             'show_email',
#             'phone',
#             'show_phone',
#             'telegram',
#             'show_telegram',
#             'other_contact',
#             'description',
#         ]
#
#         exclude = ['user']

class EditProfile(forms.ModelForm):
    # username = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)

    class Meta:
        model = Profile
        # fields = ('username', 'email', 'first_name', 'last_name')
        fields = [
            'gender',
            'birth_date',
            'show_email',
            'phone',
            'show_phone',
            'telegram',
            'show_telegram',
            'other_contact',
            'description',
            ]
        exclude = ['user']
    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')

        # if email and User.objects.filter(email=email).exclude(username=username).count():
        #     raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        # return email

    def save(self, commit=True):
        user = super(EditProfile, self).save(commit=False)
        if self.cleaned_data['gender']:
            user.profile.gender = self.cleaned_data['gender']
        if self.cleaned_data['telegram']:
            user.profile.telegram = self.cleaned_data['telegram']
        if self.cleaned_data['show_telegram']:
            user.profile.show_telegram = self.cleaned_data['show_telegram']
        if self.cleaned_data['birth_date']:
            user.profile.birth_date = self.cleaned_data['birth_date']
        if self.cleaned_data['show_email']:
            user.profile.show_email = self.cleaned_data['show_email']
        if self.cleaned_data['phone']:
            user.profile.phone = self.cleaned_data['phone']
        if self.cleaned_data['show_phone']:
            user.profile.show_phone = self.cleaned_data['show_phone']
        if self.cleaned_data['other_contact']:
            user.profile.other_contact = self.cleaned_data['other_contact']
            user.profile.description = self.cleaned_data['description']
        if commit:
            user.profile.save()
        return user

class EditUser(forms.ModelForm):
    # username = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name']
        exclude = ['user']

    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')

    # if email and User.objects.filter(email=email).exclude(username=username).count():
    #     raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    # return email

    def save(self, commit=True):
        user = super(EditProfile, self).save(commit=False)
        if self.cleaned_data['gender']:
            user.profile.gender = self.cleaned_data['gender']
        if self.cleaned_data['telegram']:
            user.profile.telegram = self.cleaned_data['telegram']
        if self.cleaned_data['show_telegram']:
            user.profile.show_telegram = self.cleaned_data['show_telegram']
        if self.cleaned_data['birth_date']:
            user.profile.birth_date = self.cleaned_data['birth_date']
        if self.cleaned_data['show_email']:
            user.profile.show_email = self.cleaned_data['show_email']
        if self.cleaned_data['phone']:
            user.profile.phone = self.cleaned_data['phone']
        if self.cleaned_data['show_phone']:
            user.profile.show_phone = self.cleaned_data['show_phone']
        if self.cleaned_data['other_contact']:
            user.profile.other_contact = self.cleaned_data['other_contact']
            user.profile.description = self.cleaned_data['description']
        if commit:
            user.profile.save()
        return user