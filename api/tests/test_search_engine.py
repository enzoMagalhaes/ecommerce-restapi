

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
			amount_sold=200,
			is_promotion=False,
			discount_rate=None,
			category="Eletronicos",
			national=True,
			free_shipping=True,
			is_new=True,
			rating=4
		)

		test_product3 = Product.objects.create(
			id=3,
			name="a random name",
			description="a nice product",
			quantity=5,
			price=400.50,
			img=None,
			amount_sold=200,
			is_promotion=False,
			discount_rate=None,
			category="Relogios",
			national=True,
			free_shipping=True,
			is_new=True,
			rating=4
		)

	def test_product_search_view(self):
		path  = reverse('search_endpoint')

		single_output_search_terms = ['test_product2','test_description2','random','nice']
		multiple_output_search_terms = ['test_product','test',"test_description"]

		for term in single_output_search_terms:

			query_parameter = {"search":term}
			response = self.client.get(path,query_parameter)

			data = response.data
			is_single_output = isinstance(data,list) and len(data) == 1

			self.assertEqual(response.status_code,status.HTTP_200_OK)
			self.assertEqual(is_single_output,True)

		for term in multiple_output_search_terms:

			query_parameter = {"search":term}
			response = self.client.get(path,query_parameter)

			data = response.data

			is_list_output = isinstance(data,list) and len(data) > 1

			self.assertEqual(response.status_code,status.HTTP_200_OK)
			self.assertEqual(is_list_output,True)


