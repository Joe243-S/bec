from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.gallery_page, name='about'),
    path('gallery/', views.gallery_page, name='gallery'),
]