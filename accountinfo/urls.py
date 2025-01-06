from django.urls import path
from .views import * 


urlpatterns = [
    path("<int:pk>/",ProfileGetView.as_view()),
    path("create/",ProfilePostView.as_view()),
    path("<int:pk>/edit/",ProfileUpdateView.as_view()),
]

