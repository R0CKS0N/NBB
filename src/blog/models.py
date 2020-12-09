from django.db import models

LABEL_CHOICES = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('AN', 'AfterNoon'),
)


class Gets(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    number_two = models.IntegerField(blank=True, null=True)
    Email = models.CharField(max_length=100)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    times = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
