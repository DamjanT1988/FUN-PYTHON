from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateView.as_view(), name='post-list-create'),  # Handle the /api/posts/ endpoint
    path('<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),  # Handle specific post actions
]
