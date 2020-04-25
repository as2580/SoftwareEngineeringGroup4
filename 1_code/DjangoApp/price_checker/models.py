from django.db import models
from django.db.models import DecimalField
from decimal import Decimal

# Create your models here.


class Item(models.Model):
    name = models.TextField()
    #price = models.FloatField()
    price = DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    rfid = models.FloatField()
    image = models.FilePathField(path="/img")

    def __init__(self, name, rfid, price, img):
        self.name = name
        self.rfid = rfid
        self.price = price
        self.image = img

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_rfid(self):
        return self.rfid