from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

CATEGORY_CHOICES=(
    ('FA','Fashion'),
    ('MW','Man Watches'),
    ('WW','Woman Watches'),
    ('FJ','Fine Jewelry'),
    ('EW','Engagement Wedding'),
    ('MJ','Man Jewelry'),
    ('VA','Vintage Antique'),
    ('LD','Loose Dimonds'),
    ('LD','Loose Beads'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    catagory = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    slug = models.SlugField()
    #discount = models.CharField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  reverse("Core:products" , kwargs={
            'slug':self.slug
        })

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