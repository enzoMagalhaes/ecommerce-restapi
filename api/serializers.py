
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id','name','description','price','quantity','img'
			,'amount_sold','is_promotion','discount_rate','category','national','free_shipping','is_new','rating')