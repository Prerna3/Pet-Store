from django.contrib import admin
from .models import Pet, CartItem, Order


# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = ["pet_id", "pet_name", "category", "price", "proImage"]


admin.site.register(Pet, PetAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ["pet", "quantity", "date_added"]


admin.site.register(CartItem, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "pet_id", "quantity", "user", "is_completed"]


admin.site.register(Order, OrderAdmin)
