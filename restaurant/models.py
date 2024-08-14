from django.db import models


class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining the ID field
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining the ID field
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDATE = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.BookingDATE}"

