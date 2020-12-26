from django.conf.urls import url, include
from django.urls import path, include
from .views import *
urlpatterns = [
    url(r'^$', homepage, name='home'),
    url(r'posts/post', post_page, name='post_page'),
    url(f'user/profile', user_profile, name='profile'),
    url(f'scoreboard', score_board, name='scoreboard'),
    url(f'TenYad', new_assist_post, name='TenYad'),
    path('react/<int:pk>', ReactView, name="react_to_post"),
    path('cancel_react/<int:pk>/<int:user_reaction_remove>', CancelReactView, name="cancel_react_to_post"),
    path('approve_react/<int:pk>/<int:approved_reaction>', AcceptReactView, name="accept_react_to_post"),
    path('delete_post/<int:pk>', DeletePostView, name="delete_post"),
    url(f'posts/history', post_history, name='post_history'),
    url(f'profile_edit', profile_edit, name='profile_edit'),
    ]
