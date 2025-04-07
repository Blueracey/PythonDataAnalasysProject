from django.urls import path
from . import views

urlpatterns = [
    path('', views.netflix_search, name='searchPage/netflix_search'),
]
