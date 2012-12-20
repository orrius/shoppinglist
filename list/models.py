from django.db import models

# Create your models here.

class Store(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200)

class ShoppingList(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200)
    stores = models.ManyToManyField(Store)
    

class Item(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=1)
    shoppinglist = models.ForeignKey(ShoppingList)


