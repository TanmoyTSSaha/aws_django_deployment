from django.db import models

# Create your models here.
class CRUDModel(models.Model):
    ProductName = models.CharField(null=False, max_length=1000)
    Color = models.CharField(null=False, max_length=1000)
    Category = models.CharField(null=False, max_length=1000)
    Price = models.IntegerField(null=False)