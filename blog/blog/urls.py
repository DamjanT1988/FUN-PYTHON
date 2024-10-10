from django.contrib import admin
from django.urls import path, include
from posts.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),  # Include the posts app's URLs
    path('', home),  # Set the root URL to the home view
]
