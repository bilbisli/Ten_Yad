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
        exclude = ['user', 'time_updated_last']


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'show_email',
            'gender',
            'birth_date',
            'phone',
            'show_phone',
            'telegram',
            'show_telegram',
            'other_contact',
            'description',
            ]
        exclude = ['user']

    def save(self, commit=True):
        user = super(EditProfile, self).save(commit=False)
        user.profile.show_email = self.cleaned_data['show_email']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.telegram = self.cleaned_data['telegram']
        user.profile.show_telegram = self.cleaned_data['show_telegram']
        user.profile.birth_date = self.cleaned_data['birth_date']
        user.profile.phone = self.cleaned_data['phone']
        user.profile.show_phone = self.cleaned_data['show_phone']
        user.profile.other_contact = self.cleaned_data['other_contact']
        user.profile.description = self.cleaned_data['description']
        if commit:
            user.profile.save()
        return user


class EditUser(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
                  'email',
                  ]
        exclude = ['user']

    def save(self, commit=True):
        user = super(EditUser, self).save(commit=False)
        user.profile.set_email(self.cleaned_data['email'])
        if commit:
            user.profile.save()
        return user


class ContactEmailForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

