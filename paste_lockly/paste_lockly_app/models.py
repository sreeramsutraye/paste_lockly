from django.db import models

class Snippet(models.Model):
    content = models.TextField()
    secret_key = models.CharField(max_length=256, blank=True, null=True)
