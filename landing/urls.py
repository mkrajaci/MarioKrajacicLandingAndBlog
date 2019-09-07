from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='landing-home'),  # prvi atribut je url
    path('about/', views.about, name='landing-about'),
]
