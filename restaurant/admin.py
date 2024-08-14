from django.contrib import admin

from .models import Menu, Booking  # Import the models you want to register

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)

