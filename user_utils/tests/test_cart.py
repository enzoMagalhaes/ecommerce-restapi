

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

	def get_access_token(self):
		
		path  = reverse('register')
		data = {'email':"testuser@email.com",'user_name':"testuser",'password':"password"}

		response = self.client.post(path,data)
		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		
		path = reverse('get_token')

		data = {'email':"testuser@email.com",'password':"password"}

		response = self.client.post(path,data)
		self.assertEqual(response.status_code,status.HTTP_200_OK)
		
		access_token = response.data['access']
		return access_token

	def test_add_delete_cart(self):	

		path  = reverse('addcart')

		data = {
			'product_id':"1",
		}

		access_token = self.get_access_token()

		#add cart
		response = self.client.post(path,data,HTTP_ACCEPT='application/json',HTTP_AUTHORIZATION='Bearer ' + access_token)

		self.assertEqual(response.status_code,status.HTTP_200_OK)

		#test get cart data
		path  = reverse('cart')

		response = self.client.get(path,HTTP_ACCEPT='application/json',HTTP_AUTHORIZATION='Bearer ' + access_token)

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(len(response.data),1)

		product = response.data[0]

		self.assertEqual(product['id'],1)
		self.assertEqual(product['name'],'test_product')
		self.assertEqual(product['rating'],4)


		#test delete cart product
		path  = reverse('delcart')
		response = self.client.post(path,data,HTTP_ACCEPT='application/json',HTTP_AUTHORIZATION='Bearer ' + access_token)

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(response.data['status'],"OK")

		#test if product was deleted
		path  = reverse('cart')
		response = self.client.get(path,HTTP_ACCEPT='application/json',HTTP_AUTHORIZATION='Bearer ' + access_token)

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		self.assertEqual(len(response.data),0)
