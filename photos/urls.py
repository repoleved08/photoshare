from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('viewphoto/<str:pk>/', views.viewPhoto, name='viewphoto'),
    path('addphoto/', views.addPhoto, name='addphoto'),
]
