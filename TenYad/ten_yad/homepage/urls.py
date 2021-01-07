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
    path('cancel_react/<int:pk>/<int:user_reaction_remove>/', CancelReactView, name="cancel_react_to_post"),
    path('cancel_react/<int:pk>/<int:user_reaction_remove>/<path:redirection>', CancelReactView, name="cancel_react_to_post"),
    path('approve_react/<int:pk>/<int:approved_reaction>', AcceptReactView, name="accept_react_to_post"),
    path('complete_assist/<int:pk>/<int:user_assist>', CompleteAssistView, name="complete_assist"),
    path('complete_assist/<int:pk>/<int:user_assist>/<path:redirection>', CompleteAssistView, name="complete_assist"),
    path('rate_user/<int:pk>/<int:user_rate>/<int:amount_rate>', rate_user_view, name="rate_user"),
    path('delete_post/<int:pk>', DeletePostView, name="delete_post"),
    path('close_post/<int:pk>', ClosePostView, name="close_post"),
    path('reactivate_post/<int:pk>', ReactivatePostView, name="reactivate_post"),
    url(f'posts/history', post_history, name='post_history'),
    url(f'profile_edit', profile_edit, name='profile_edit'),
    url(f'Messages', Messages, name='Messages'),
    url(f'change_password', change_password, name='change_password'),
    url(f'edit_post', edit_post, name='edit_post'),
    path('certificate', certificate, name='certificate'),
    url(f'contact_admin', contact_admin, name='contact_admin'),
    url(f'volunteers', SearchVolunteersView, name='volunteers'),
    path('certificate', certificate, name='certificate'),
    ]
