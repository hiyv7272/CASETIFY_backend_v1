from django.urls import path
from .views import CartView, CheckoutView, CheckoutDetailView

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/checkout', CheckoutView.as_view()),
    path('/checkout/detail', CheckoutDetailView.as_view()),
]
