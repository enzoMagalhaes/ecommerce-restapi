

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestProductEndpoints(APITestCase):

	def test_logout(self):	
		path  = reverse('register')

		data = {

			'email':"testuser@email.com",
			'user_name':"testuser",
			'password':"password"

		}

		response = self.client.post(path,data)

		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		
		path = reverse('get_token')

		data = {
			'email':"testuser@email.com",
			'password':"password"
		}

		response = self.client.post(path,data)

		self.assertEqual(response.status_code,status.HTTP_200_OK)
		
		data = response.data
		access_token = data['access']
		refresh_token = data['refresh']

		self.assertNotEqual(access_token,None)
		self.assertNotEqual(refresh_token,None)

		path = reverse('logout')

		data = {"refresh_token":refresh_token}
		response = self.client.post(path,data,HTTP_ACCEPT='application/json',HTTP_AUTHORIZATION='Bearer ' + access_token)
		self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


		path = reverse('refresh_token')
		data = {"refresh":refresh_token}
		response = self.client.post(path,data)
		self.assertNotEqual(response.status_code,status.HTTP_200_OK)


