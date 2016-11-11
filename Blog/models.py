from __future__ import unicode_literals

from django.db import models


class MyBlog(models.Model):
    name = models.CharField(max_length=20)
    paragraph = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name