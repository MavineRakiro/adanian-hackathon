from django.db import models

class Devsinfo(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password = models.CharField(max_length =50)
    linkedin = models.URLField(max_length = 200)
    github = models.URLField(max_length=200)
    joined_at = models.DateTimeField(auto_now_add=True)