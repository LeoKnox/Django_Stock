from django.db import models

class Room(models):
    name = models.CharField(max_length=50)
    floor = models.CharField(max_lenght=50)
    description = models.TextField(blank=True)
    width = models.IntegerField();
    length = models.InterField();
    submission_date = models.DateTimeField()