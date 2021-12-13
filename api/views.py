
from rest_framework import generics
from .models import Product
from rest_framework import filters
from .serializers import ProductSerializer
from django.db.models import Q


class ProductsList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class GetProduct(generics.RetrieveDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductSearchView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name', 'description']


class ProductFilterView(generics.ListAPIView):
	serializer_class = ProductSerializer


	categories = [
		'Celulares',
		'Eletronicos',		
		'Relogios',
		'Calcados',
		'Bolsas',
		'Roupas'
	]

	def get_queryset(self):
		category = self.request.query_params.get('category',self.categories)
		national = self.request.query_params.get('national',[True,False])
		is_promotion = self.request.query_params.get('is_promotion',[True,False])
		free_shipping = self.request.query_params.get('free_shipping',[True,False])
		min_price = self.request.query_params.get('min_price',0)
		max_price = self.request.query_params.get('max_price',99999999999) #max_digits=10
		is_new = self.request.query_params.get('is_new',[True,False])
		rating = self.request.query_params.get('rating',[0,1,2,3,4,5])


		# the __in django search category requires the input to be list, so if the input is just a  single value
		# (like a string or a bool value) we turn it into a list with a single value , and thats what the code below does.
		if isinstance(category,str):
			category = [category]

		bool_filters = [national,is_promotion,free_shipping,is_new,rating]
		for i in range(len(bool_filters)):
			feature = bool_filters[i]


			if feature == 'true':
				bool_filters[i] = [True]
			elif feature == 'false':
				bool_filters[i] = [False]


		#filtering...
		return Product.objects.filter(
			category__in=category, national__in=bool_filters[0], is_promotion__in=bool_filters[1],
			free_shipping__in=bool_filters[2],price__range=[min_price,max_price],is_new__in=bool_filters[3],rating__in=bool_filters[4]
			)
