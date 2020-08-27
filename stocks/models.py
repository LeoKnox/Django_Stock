from django.db import models

class Room(models.Model):
    LIGHT = [('on', 'On'), ('off', 'Off')]
    name = models.CharField(max_length=50)
    floor = models.CharField(max_lenght=50)
    description = models.TextField(blank=True)
    width = models.IntegerField();
    length = models.IntegerField();
    lighting = models.CharField(max_length=3, choices=LIGHT)
    submission_date = models.DateTimeField()
    doors = models.ManyToManyField('Door')

class Door(models.Model):
    WALL = [('N', 'North'),('E', 'East'),('S', 'South'),('W','West')]
    material = models.CharField(max_length=50)
    wall = models.CharField(max_lenght=1, choices="WALL")
    location = models.IntegerField();