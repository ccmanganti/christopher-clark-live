# THIS IS THE APP LEVEL URL ROUTING
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
]
