

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
			price=2000,
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
			price=400,
			img=None,
			amount_sold=200,
			is_promotion=False,
			discount_rate=None,
			category="Eletronicos",
			national=True,
			free_shipping=False,
			is_new=True,
			rating=4
		)

		test_product3 = Product.objects.create(
			id=3,
			name="a random name",
			description="a nice product",
			quantity=5,
			price=10000,
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


	parameters={
			'celulares' :False , 
            'eletronicos' :False ,
            'relogios' :False ,
            'calcados' :False ,
            'bolsas' :False ,
            'roupas' :False ,
            'nacional' :False ,
            'importado' :False ,
            'novo' :False ,
            'usado' :False ,
            'promocao' :False ,
            'frete_gratis' :False ,
            'min_price' :'null',
            'max_price' :'null',
            'rating' :'null'			
	}

	path  = reverse('filter_endpoint')

	def test_filter_categories(self):

		filters = ['celulares',
				   'relogios',
				   'eletronicos',
				   ['celulares','eletronicos'],
				   ['celulares','relogios','eletronicos']
				  ]

		for filter_argument in filters:

			query_parameter = self.parameters.copy()
			
			if isinstance(filter_argument,str):

				query_parameter[filter_argument] = 'true'
				response = self.client.get(self.path,query_parameter)

				self.assertEqual(response.status_code,status.HTTP_200_OK)
				self.assertEqual(len(response.data),1)
			elif isinstance(filter_argument,list):

				for term in filter_argument:
					query_parameter[term] = 'true'

				response = self.client.get(self.path,query_parameter)

				self.assertEqual(response.status_code,status.HTTP_200_OK)
				self.assertEqual(len(response.data),len(filter_argument))

	def test_min_max_filter(self):

		filters = [{"filter":{'max_price':500},"len":1},
				   {"filter":{"min_price":500,'max_price':3000},"len":1},
				   {"filter":{"min_price":9000},"len":1},
				   {"filter":{"max_price":9000},"len":2},
				   {"filter":{"min_price":1,'max_price':9000},"len":2},
				   {"filter":{"min_price":500},"len":2},
				  ]

		for filter_argument in filters:

			query_parameter = self.parameters.copy()
			query_parameter.update(filter_argument['filter'])

			response = self.client.get(self.path,query_parameter)

			self.assertEqual(response.status_code,status.HTTP_200_OK)
			self.assertEqual(len(response.data),filter_argument['len'])


	def test_filter_promotion_shipping(self):

		filters = [
				   {"filter":{'promocao':'true'},"len":1},
				   {"filter":{'promocao':'false',"frete_gratis":'true'},"len":2},
				   {"filter":{'promocao':'true',"frete_gratis":'false'},"len":1},
				  ]

		for filter_argument in filters:

			query_parameter = self.parameters.copy()
			query_parameter.update(filter_argument['filter'])

			response = self.client.get(self.path,query_parameter)

			self.assertEqual(response.status_code,status.HTTP_200_OK)
			self.assertEqual(len(response.data),filter_argument['len'])

