from django import forms
from .models import Post


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
