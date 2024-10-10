from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to the Blog API</h1><p>Go to <a href='/api/posts/'>Posts</a></p>")

# List all posts and create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Retrieve, update, or delete a post by ID
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

