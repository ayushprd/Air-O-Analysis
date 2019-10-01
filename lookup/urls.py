from django.urls import path
from . import views #importing views from this folder
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]

