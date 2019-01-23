from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('article/<int:pk>', views.detail, name='detail'),
    path('contacts/', views.contacts, name='contacts'),
]
