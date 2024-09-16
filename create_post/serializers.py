from rest_framework import serializers
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "required_amount",
            "get_image",
            "get_thumbnail"
        )
