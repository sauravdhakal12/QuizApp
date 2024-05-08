from django.urls import path
from . import views

urlpatterns = [
  path("home", views.home),
  path("post", views.post),
  path("post_detail", views.post_detail),
]