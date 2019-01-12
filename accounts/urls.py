from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path

from .decorators import check_recaptcha
from . import views


urlpatterns = [
    path('signup/', check_recaptcha(views.RegisterView.as_view()), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
