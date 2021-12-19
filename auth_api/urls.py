

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register',views.RegisterUser.as_view()),
    path('logout',views.LogoutToken.as_view()),
    path('check_token',views.CheckToken.as_view())
]

