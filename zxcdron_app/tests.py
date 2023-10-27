from django.test import TestCase
from .models import OrderManager

o = OrderManager()
o.add_name('sv')
o.add_phone('324')
o.add_address('324dvs')

