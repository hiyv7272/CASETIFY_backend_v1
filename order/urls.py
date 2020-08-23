from django.urls import path
from .views import CartView, OrderView, OrderDetailView

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/order', OrderView.as_view()),
    path('/detail', OrderDetailView.as_view()),
]
