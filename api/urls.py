from django.urls import path, include
from django.contrib.auth.models import User
from .views import UserView, UserListView


urlpatterns = [
    path(r'users/<int:pk>/', UserView.as_view()),
    path(r'users/', UserListView.as_view()),
]
