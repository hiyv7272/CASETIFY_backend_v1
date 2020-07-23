from django.urls import path
from .views import Cart, OrderView, OrderCheckoutView

urlpatterns = [
    path('/cart', Cart.as_view()),
    path('/orderview', OrderView.as_view()),
    path('/ordercheckout', OrderCheckoutView.as_view()),
]
