from django.contrib.auth.models import User
from django.db import models


class Translation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    result = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
