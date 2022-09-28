from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import Http404
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomePageView(TemplateView):
    template_name = "home_page.html"
