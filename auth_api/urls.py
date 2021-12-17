

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register',views.RegisterUser.as_view())
]

