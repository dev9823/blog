from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.BlogCreateView.as_view(), name="create"),
]