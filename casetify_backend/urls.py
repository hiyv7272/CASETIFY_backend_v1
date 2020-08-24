from django.urls import path, include
from .views import FileToUrl

urlpatterns = [
    path('user', include('user.urls')),
    path('order', include('order.urls')),
    path('artwork', include('artwork.urls')),
    path('image_upload', FileToUrl.as_view()),
]