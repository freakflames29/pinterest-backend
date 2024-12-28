from django.urls import path
from . import  views
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path("signup/",views.UserView.as_view()),
    path("token/",TokenObtainPairView.as_view()),
    path("login/",views.LoginView.as_view()),
    path("refresh/",TokenRefreshView.as_view()),
]