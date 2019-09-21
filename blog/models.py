from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # Add timestamp using time zone from settings.py
    date = models.DateTimeField(auto_now_add=True)
    # Author is the custom user model (users app)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[str(self.id)])