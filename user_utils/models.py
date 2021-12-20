from django.db import models
from auth_api.models import NewUser
from api.models import Product


class WishList(models.Model):
    
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)

    def __str__(self):
    	return f"{self.user} - {self.product} - WISH"


class History(models.Model):
    
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
    	return f"{self.user} - {self.product} - HISTORY"