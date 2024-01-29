from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


# Create your models here.
class CustomeManager(models.Manager):
    def get_price_range(self, r1, r2):
        return self.filter(price__range=(r1, r2))

    def doglist(self):
        return self.filter(category__exact="Dog")

    def catlist(self):
        return self.filter(category__exact="Cat")

    def birdlist(self):
        return self.filter(category__exact="Bird")

    def fishlist(self):
        return self.filter(category__exact="Fish")


class Pet(models.Model):
    pet_id = models.IntegerField(primary_key="True")
    pet_name = models.CharField(max_length=50)
    type = (("Cat", "Cat"), ("Dog", "Dog"), ("Bird", "Bird"), ("Fish", "Fish"))
    category = models.CharField(max_length=100, choices=type)
    desc = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to="pics")

    pet = CustomeManager()  # customer manager
    objects = models.Manager()  # default manager

    def proImage(self):
        return mark_safe(f"<img src='{self.image.url}' width='300px'>")


class CartItem(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Order(models.Model):
    order_id = models.CharField(max_length=50)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default="False")
