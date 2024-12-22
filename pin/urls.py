from django.urls import path
from .views import *

urlpatterns = [
    path("",PinListView.as_view())
]
