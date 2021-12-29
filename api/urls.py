

from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductsList.as_view(),name="products_list"),
    path('<int:pk>',views.GetProduct.as_view(), name="get_product"),
    path('search',views.ProductSearchView.as_view(),name="search_endpoint"),
    path('filter',views.ProductFilterView.as_view(),name="filter_endpoint")
]