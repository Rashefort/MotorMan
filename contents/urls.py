from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('profile/', views.profile, name='profile'),
    path('contacts/', views.contacts, name='contacts'),
]