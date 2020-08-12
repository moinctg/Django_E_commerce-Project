from django.db import models
from django.contrib.auth.models import User
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username