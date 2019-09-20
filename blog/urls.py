from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog-home'),  # prvi atribut je url
    path('about/', views.about, name='blog-about'),
]
