

from django.urls import path
from . import views


urlpatterns = [
    path('wishlist',views.UserWishList.as_view()),
    path('history',views.UserHistory.as_view()),
    path('addwish',views.AddWish.as_view()),
    path('addhistory',views.AddHistory.as_view()),
    path('delwish',views.DelWish.as_view()),
]
