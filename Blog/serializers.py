from rest_framework import serializers

from Blog.models import MyBlog


class MyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBlog
        fields = ('id', 'name', 'paragraph', 'created_at', 'modified_at')
