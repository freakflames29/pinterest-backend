from django.urls import path
from .views import * 


urlpatterns = [
    path("",ProfileGetView.as_view()),
    path("create/",ProfilePostView.as_view()),
    path("<int:pk>/edit/",ProfileUpdateView.as_view()),
    path("update/",ProfileUpdateV2.as_view()),
]

