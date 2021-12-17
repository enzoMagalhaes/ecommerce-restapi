
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

		categories = []
		national = []
		is_new = []


		categories.append(('Celulares',self.request.query_params.get('celulares',False)))
		categories.append(('Eletronicos',self.request.query_params.get('eletronicos',False)))
		categories.append(('Relogios',self.request.query_params.get('relogios',False)))
		categories.append(('Calcados',self.request.query_params.get('calcados',False)))
		categories.append(('Bolsas',self.request.query_params.get('bolsas',False)))
		categories.append(('Roupas',self.request.query_params.get('roupas',False)))

		national.append((True,self.request.query_params.get('nacional',False)))
		national.append((False,self.request.query_params.get('importado',False)))

		is_new.append((True,self.request.query_params.get('novo',False)))
		is_new.append((False,self.request.query_params.get('usado',False)))

		promocao = self.request.query_params.get('promocao',False)
		frete_gratis = self.request.query_params.get('frete_gratis',False)

		bool_filters = {'category':[],'national':[],'is_promotion':[],'free_shipping':[],'is_new':[]}
		


		for category in categories:
			if category[1] == 'true':
				bool_filters['category'].append(category[0])

		if len(bool_filters['category']) == 0:
			bool_filters['category'].extend(self.categories)





		for feature in national:
			print(feature)
			if feature[1] == 'true':
				bool_filters['national'].append(feature[0])

		if len(bool_filters['national']) == 0:
			bool_filters['national'].extend([True,False])





		for feature in is_new:
			if feature[1] == 'true':
				bool_filters['is_new'].append(feature[0])

		if len(bool_filters['is_new']) == 0:
			bool_filters['is_new'].extend([True,False])		

		if promocao == 'true':
			bool_filters['is_promotion'].append(True)
		else:
			bool_filters['is_promotion'].extend([True,False])


		if frete_gratis == 'true':
			bool_filters['free_shipping'].append(True)
		else:
			bool_filters['free_shipping'].extend([True,False])


		min_price = self.request.query_params.get('min_price',0)
		if (min_price == 'null') :
			min_price = 0

		max_price = self.request.query_params.get('max_price',99999999999) #max_digits=10
		if (max_price == 'null') :
			max_price = 99999999999


		rating = self.request.query_params.get('rating',[0,1,2,3,4,5])
		if (rating == 'null') :
			rating = [0,1,2,3,4,5]


		#filtering...
		return Product.objects.filter(
			category__in=bool_filters['category'], national__in=bool_filters['national'], is_promotion__in=bool_filters['is_promotion'],
			free_shipping__in=bool_filters['free_shipping'],price__range=[min_price,max_price],is_new__in=bool_filters['is_new'],rating__in=rating
			)
