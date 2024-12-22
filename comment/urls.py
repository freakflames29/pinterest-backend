from django.urls import path
from . import  views


urlpatterns=[
    path("all/",views.CommentListView.as_view())
]