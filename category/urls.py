from django.urls import path
from . import views

urlpatterns = [
    path("",views.CategoryListView.as_view()),
    path("<int:pk>/pins/",views.CategorySinglePinView.as_view()),
]
