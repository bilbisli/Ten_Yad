from django.conf.urls import url, include
from django.urls import path, include
from .views import *

urlpatterns = [
    url(r'^$', homepage, name='home'),
    url(r'posts/post', post, name='post'),
    url(f'user/profile', user_profile, name='profile'),
    url(f'scoreboard', score_board, name='scoreboard'),
    url(f'TenYad', new_assist_post, name='TenYad'),
]
