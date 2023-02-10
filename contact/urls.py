from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import loginView, index, registration
urlpatterns = [
    path("login/", loginView, name="loginView"),
    path("", index, name="index"),
    path("logout/", LogoutView.as_view(next_page="/login/"), name="logout"),
    path("registration/", registration, name="registration" )
]
