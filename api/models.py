from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Product(models.Model):

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	quantity = models.PositiveIntegerField()
	price = models.DecimalField(decimal_places=2,max_digits=10)
	img = models.ImageField(null=True,blank=True)
	amount_sold = models.PositiveIntegerField(default=0)
	is_promotion = models.BooleanField(default=False)
	discount_rate = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=3)

	categories = (

		('Celulares','celulares'),
		('Eletronicos','eletronicos'),
		('Relogios','relogios'),
		('Calcados','calcados'),
		('Bolsas','bolsas'),
		('Roupas','roupas'),

	)

	category = models.CharField(max_length=12,choices=categories)
	national = models.BooleanField(default=True)
	free_shipping= models.BooleanField(default=False)
	is_new = models.BooleanField(default=True)
	rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])



	def __str__(self):
		return f"{self.name} - {self.price}"