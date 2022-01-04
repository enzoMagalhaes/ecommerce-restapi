

from django.urls import path
from . import views


urlpatterns = [
    path('wishlist',views.UserWishList.as_view(),name="wishlist"),
    path('history',views.UserHistory.as_view(),name="history"),
    path('cart',views.UserCart.as_view(),name="cart"),

    path('addwish',views.AddWish.as_view(),name="addwish"),
    path('addhistory',views.AddHistory.as_view(),name="addhistory"),
    path('addcart',views.AddToCart.as_view(),name="addcart"),

    path('delwish',views.DelWish.as_view(),name="delwish"),
    path('delcart',views.DelCartItem.as_view(),name="delcart"),

    path('make_transaction',views.MakeTransaction.as_view(),name="make_transaction"),
]

