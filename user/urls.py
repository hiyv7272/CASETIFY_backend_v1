from django.urls import path 
from .views import (
    SignUpView, 
    SignInView, 
    MyProfileView,
    MyShippingInfoView,
    KakaologinView,
)

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/myprofile', MyProfileView.as_view()),
    path('/myshippinginfo', MyShippingInfoView.as_view()),
    path('/kakaologin', KakaologinView.as_view()),
]