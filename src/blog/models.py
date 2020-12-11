from django.db import models


class Gets(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    number_two = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100)
    times = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
