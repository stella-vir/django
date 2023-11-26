from django.test import TestCase
from django.urls import reverse
from .models import Product

class UrlResolveTestCase(TestCase):
    def test_product_list_url_resolves(self):
        url = reverse('product-list-api')  # Change to the name of your URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url_resolves(self):
        # Replace '1' with an existing product ID in your database
        url = reverse('product-detail-api', args=[1])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ProductCRUDTestCase(TestCase):
    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'Description of test product',
            'price': 29.99
        }
        self.updated_data = {
            'name': 'Updated Test Product',
            'description': 'Updated description',
            'price': 39.99
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        # Ensure product was created successfully
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.description, 'Description of test product')
        self.assertEqual(product.price, 29.99)

    def test_update_product(self):
        # Update the product and check if the changes are reflected
        self.product.name = self.updated_data['name']
        self.product.description = self.updated_data['description']
        self.product.price = self.updated_data['price']
        self.product.save()

        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, 'Updated Test Product')
        self.assertEqual(updated_product.description, 'Updated description')
        self.assertEqual(updated_product.price, 39.99)

    def test_show_product(self):
        # Retrieve and verify the details of the created product
        retrieved_product = Product.objects.get(id=self.product.id)
        self.assertEqual(retrieved_product.name, 'Test Product')

    def test_delete_product(self):
        # Delete the product and ensure it no longer exists in the database
        product_to_delete = Product.objects.get(id=self.product.id)
        product_to_delete.delete()

        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)
