from django.urls import path 
from .views import ArtworkListView, ArtworkDetailView

urlpatterns = [
    path('/list', ArtworkListView.as_view()),
    path('/detail', ArtworkDetailView.as_view()),
]
