from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),  # prvi atribut je url
]