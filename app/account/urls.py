from django.urls import path
from account.views import *

urlpatterns = [
    path('login', Login.as_view()),
]
