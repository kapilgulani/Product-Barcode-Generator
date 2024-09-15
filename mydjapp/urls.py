from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("about/", views.about),
    path("register/", views.register),
    path("search/", views.search),
    path("myadmin/", views.myadmin),
    path("manageusers/", views.manageusers),
    path("user/", views.user)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
