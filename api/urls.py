from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .views import UserView

router = routers.SimpleRouter()
router.register(r'users', UserView)
urlpatterns = router.urls
