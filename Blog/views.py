from django.shortcuts import render
from rest_framework import generics

from Blog.models import MyBlog
from Blog.serializers import MyBlogSerializer


class ListcreateMyBlog(generics.ListCreateAPIView):

    queryset = MyBlog.objects.all()
    serializer_class = MyBlogSerializer
