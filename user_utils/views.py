
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProductSerializer
from api.models import Product
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


from .models import WishList,History,CartItem

class UserWishList(APIView):
	permission_classes = [IsAuthenticated]

	def get(self,request):

		products = []

		for wish in  WishList.objects.filter(user=request.user):
			product = wish.product
			product = ProductSerializer(product)

			products.append(product.data)

		return Response(products)


class UserHistory(APIView):
	permission_classes = [IsAuthenticated]

	def get(self,request):
		products = []

		for history in  History.objects.filter(user=request.user):
			product = history.product
			product = ProductSerializer(product)

			products.append(product.data)

		return Response(products)


class UserCart(APIView):
	permission_classes = [IsAuthenticated]

	def get(self,request):
		products = []

		for item in  CartItem.objects.filter(user=request.user):
			product = item.product
			product = ProductSerializer(product)

			products.append(product.data)

		return Response(products)


class AddWish(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):

		product_id = request.data.get('product_id')
		product = Product.objects.get(id=product_id)

		try:
			instance = WishList.objects.create(user=request.user,product=product)
			instance.save()
			return Response({"status":'OK'})
		except IntegrityError as e:
			return Response({"detail":"Product already exists in wishlist"})



class AddHistory(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):
		
		product_id = request.data.get('product_id')
		product = Product.objects.get(id=product_id)

		instance = History.objects.create(user=request.user,product=product)
		instance.save()
		return Response({"status":'OK'})



class AddToCart(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):

		product_id = request.data.get('product_id')
		product = Product.objects.get(id=product_id)

		instance = CartItem.objects.create(user=request.user,product=product)
		instance.save()
		return Response({"status":'OK'})



class DelWish(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):

		product_id = request.data.get('product_id')
		product = Product.objects.get(id=product_id)

		try:
			instance = WishList.objects.get(user=request.user,product=product)
			instance.delete()
			return Response({"status":'OK'})
		except ObjectDoesNotExist as e:
			return Response({"detail":"Product does not exist in wishlist"})



class DelCartItem(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):

		product_id = request.data.get('product_id')
		print("PRODUTO: " +product_id)
		product = Product.objects.get(id=product_id)

		try:
			instance = CartItem.objects.filter(user=request.user,product=product)
			instance.delete()
			return Response({"status":'OK'})
		except ObjectDoesNotExist as e:
			return Response({"detail":"Product does not exist in Cart"})



class MakeTransaction(APIView):
	permission_classes = [IsAuthenticated]

	def post(self,request):

		instance = CartItem.objects.filter(user=request.user)

		for row in instance:

			history_product = History.objects.create(user=request.user,product=row.product)
			history_product.save()


		instance.delete()
		return Response({"detail":"transaction complete"})

    # const data = {
    #   Nome:Nome,
    #   Sobrenome:Sobrenome,
    #   Estado:Estado,
    #   CEP:CEP,
    #   Endereco:Endereco,
    #   Numero:Numero,
    #   Complemento:Complemento,
    #   Bairro:Bairro,
    #   Cidade:Cidade,
    #   Cartao:Cartao,
    #   CartaoNome:CartaoNome,
    #   CPF:CPF,
    #   MM:MM,
    #   AA:AA,
    #   CVV:CVV,
    # }

		