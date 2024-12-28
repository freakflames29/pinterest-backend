from django.urls import path
from . import views

urlpatterns = [
    path("",views.BoardView.as_view()),
    path("<int:pk>/",views.BoardSingleView.as_view()),
    path("<int:pk>/pins/",views.BoardPinsView.as_view()),
    path("<int:boardid>/pin/<int:pinid>/save/",views.AddPinToBoardView.as_view()),
]