from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    table_number = models.IntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
