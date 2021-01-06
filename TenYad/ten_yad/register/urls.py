from django.conf.urls import url, include
from django.urls import path, include
from .views import *

urlpatterns = [
    url(r'^$', register, name='register'),
]
