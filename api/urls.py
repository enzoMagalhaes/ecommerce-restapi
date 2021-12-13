

from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductsList.as_view()),
    path('<int:pk>',views.GetProduct.as_view()),
    path('search',views.ProductSearchView.as_view()),
    path('filter',views.ProductFilterView.as_view())
]