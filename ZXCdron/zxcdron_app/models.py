from django.db import models


class State(models.TextChoices):
    BUSY = 'Занят'
    FREE = 'Свободен'


class Drone(models.Model):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

    DRONE_TYPE = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )

    drone_id = models.CharField(max_length=30)
    drone_type = models.CharField(
        max_length=7,
        choices=DRONE_TYPE,
        default=MEDIUM
    )
    drone_is_free = models.CharField(
        max_length=9,
        choices=State.choices,
        default=State.FREE
    )
    power = models.CharField(max_length=4)
    weight = models.CharField(max_length=30)

    def __str__(self):
        return self.drone_id


class Places(models.Model):
    place_id = models.CharField(max_length=100)
    place_address = models.CharField(max_length=200, default='test')
    number_of_drones = models.IntegerField()
    all_drones_id = models.ManyToManyField(Drone)

    def __str__(self):
        return self.place_id


class Order(models.Model):
    place_id = models.CharField(max_length=5, default='test')
    receiver_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    used_places = models.ForeignKey(Places, on_delete=models.PROTECT, default='1')
    date = models.CharField(max_length=20, default='1111-11-11 11:11')

