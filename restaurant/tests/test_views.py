# restaurant/tests/test_views.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create an APIClient instance for making requests
        self.client = APIClient()

        # Create test Menu instances
        self.menu1 = Menu.objects.create(title="Pizza", price=9.99, inventory=100)
        self.menu2 = Menu.objects.create(title="Burger", price=5.49, inventory=50)
        self.menu3 = Menu.objects.create(title="Pasta", price=8.99, inventory=75)
    
    def test_getall(self):
        # Send a GET request to retrieve all Menu objects
        response = self.client.get('/restaurant/menu/items/')
        
        # Retrieve all menu items from the database
        menu_items = Menu.objects.all()
        
        # Serialize the menu items
        serializer = MenuSerializer(menu_items, many=True)
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the serialized data matches the response data
        self.assertEqual(response.data, serializer.data)
