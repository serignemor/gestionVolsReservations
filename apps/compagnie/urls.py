from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.compagnie import views

urlpatterns = [
    path('', views.index, name='compagnie_list'),
    path('create/', views.create, name='compagnie_create'),
    path('edit/<int:pk>/', views.edit, name='compagnie_edit'),
    path('delete/<int:pk>/', views.edit, name='compagnie_delete'),
]

#
# if settings.DEBUG:  # new
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)