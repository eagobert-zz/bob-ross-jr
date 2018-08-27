from django.db import models

# Create your models here.
class Birthday(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()  # default date format is YYYY-MM-DD
    greeting = models.TextField()