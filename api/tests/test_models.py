

from django.urls import reverse
from mixer.backend.django import mixer
from api import views
from rest_framework import status
from rest_framework.test import APITestCase

# from api.models import Product

class TestProductEndpoints(APITestCase):

	def test_products_list_view(self):
		path  = reverse('products_list')
		response = self.client.get(path,format="json")

		self.assertEqual(response.status_code,status.HTTP_200_OK)


	# def test_get_product_view(self):
	# 	path  = reverse('get_product')
	# 	response = self.client.get(path,format="json")

	# 	self.assertEqual(response.status_code,status.HTTP_200_OK)


	# def test_product_search_view(self):
	# 	path  = reverse('search_endpoint')
	# 	response = self.client.get(path,format="json")

	# 	self.assertEqual(response.status_code,status.HTTP_200_OK)


	# def test_filter_view(self):
	# 	path  = reverse('filter_endpoint')
	# 	response = request_factory.get(path,format="json")

	# 	self.assertEqual(response.status_code,status.HTTP_200_OK)

