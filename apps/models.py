from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    image = ResizedImageField(upload_to='products/images/', size=[1000, 800], crop=['middle', 'center'])
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self) -> str:
        return self.products.__str__()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name

