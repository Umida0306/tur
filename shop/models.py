from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField()
    logo = models.ImageField(upload_to='stores/')

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_top_selling = models.BooleanField(default=False)
    is_on_sale = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)

    def __str__(self):
        return self.name
