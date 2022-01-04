

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Product

class TestProductEndpoints(APITestCase):

	@classmethod
	def setUpTestData(cls):
		test_product = Product.objects.create(
			id=1,
			name="test_product",
			description="test_description",
			quantity=5,
			price=400.50,
			img=None,
			amount_sold=200,
			is_promotion=True,
			discount_rate=0.25,
			category="Celulares",
			national=True,
			free_shipping=True,
			is_new=True,
			rating=4
		)

		test_product2 = Product.objects.create(
			id=2,
			name="test_product2",
			description="test_description2",
			quantity=5,
			price=400.50,
			img=None,
			amount_sold=223,
			is_promotion=False,
			discount_rate=None,
			category="Eletronicos",
			national=True,
			free_shipping=True,
			is_new=True,
			rating=4
		)


	def test_products_list_view(self):
		path  = reverse('products_list')
		response = self.client.get(path)

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(len(response.data),2)


	def test_get_product_view(self):
		path  = reverse('get_product',kwargs={'pk':1})
		response = self.client.get(path)

		data = response.data

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(data['id'],1)
		self.assertEqual(data['name'],'test_product')
		self.assertEqual(data['amount_sold'],200)

		path  = reverse('get_product',kwargs={'pk':2})
		response = self.client.get(path)

		data = response.data

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(data['id'],2)
		self.assertEqual(data['name'],'test_product2')
		self.assertEqual(data['amount_sold'],223)



