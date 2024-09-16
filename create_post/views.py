from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class EmergencyPostsList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
