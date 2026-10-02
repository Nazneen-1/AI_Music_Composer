from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),
    path("app/", views.index, name="app"),
    path("generate/", views.generate_music, name="generate_music"),
    path("download/<int:comp_id>/", views.download_music, name="download_music"),
    path("favorite/<int:comp_id>/", views.toggle_favorite, name="toggle_favorite"),

    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", views.signup, name="signup"),
]
