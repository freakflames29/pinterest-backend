from django.urls import path
from .views import *

urlpatterns = [
    path("",PinListView.as_view()),
    path("create/",PinCreateView.as_view()),
    path("<int:pk>/",PinSingleView.as_view()),
    path("<int:pk>/comments/",CommentListView.as_view()),

]
