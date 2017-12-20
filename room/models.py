from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    tel = models.CharField(max_length=15)

    def avg_salary(self):
        return self.human_set.aggregate(models.Avg('salary'))['salary__avg']

    def __str__(self):
        return self.name


class Key(models.Model):
    human = models.ForeignKey("human.Human", blank=True, null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.human, self.room)
