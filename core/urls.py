# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),                  # Django admin route
    path("auth/", include("apps.authentication.urls")),    # Auth routes - login / register
    path("compagnie/", include("apps.compagnie.urls")),
    path("home/", include("apps.home.urls")),              # UI Kits Html files
]




if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)