
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("myauth.urls")),
    path("board/", include("board.urls")),
    path("pin/", include("pin.urls")),
    path("comments/", include("comment.urls")),
    path("profile/",include("accountinfo.urls")),
    path("category/",include("category.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
