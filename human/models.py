from django.db import models

from room.models import Room


class Human(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)