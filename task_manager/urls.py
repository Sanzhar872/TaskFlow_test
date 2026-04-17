# task_manager/urls.py  (корневой)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",   include("core.urls")),   # все эндпоинты под /api/
]