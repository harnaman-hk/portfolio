from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="site-home"),
    path('projects/', views.projects, name="project-home"),
]

