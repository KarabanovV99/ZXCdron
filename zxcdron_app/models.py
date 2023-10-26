from django.db import models


class Drone(models.Model):
    drone_id = models.CharField(max_length=100)
    drone_is_free = models.BooleanField()
    power = models.FloatField()
    weight = models.CharField(max_length=100)

    def __str__(self):
        return self.drone_id


class Places(models.Model):
    place_id = models.CharField(max_length=100)
    number_of_drones = models.IntegerField()
    number_of_free_drones = models.IntegerField()

    def __str__(self):
        return self.place_id


