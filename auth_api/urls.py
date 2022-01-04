

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(),name="get_token"),
    path('token/refresh', TokenRefreshView.as_view(),name="refresh_token"),
    path('register',views.RegisterUser.as_view(),name="register"),
    path('logout',views.LogoutToken.as_view(),name="logout"),
    path('check_token',views.CheckToken.as_view(),name="check_token")
]

