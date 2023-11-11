# to jest główny urls

from django.contrib import admin
from django.urls import path, include

from mathematics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("mathematics.urls")),
    path("", include("blog.urls")),
]
