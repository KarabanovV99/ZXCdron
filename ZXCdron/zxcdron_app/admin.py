from django.contrib import admin
from .models import Drone, Places, Order


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ['drone_id', 'drone_type', 'drone_is_free', 'power', 'weight']
    ordering = ['-power', 'drone_is_free']
    # readonly_fields = ['drone_is_free', 'power']


@admin.register(Places)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_id', 'place_address', 'number_of_drones']
    filter_horizontal = ['all_drones_id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'receiver_name', 'address', 'used_places']
