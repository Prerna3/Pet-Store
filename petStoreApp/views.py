from django.shortcuts import render, redirect
from .models import Pet, CartItem, Order
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from django.contrib import messages
import random


# Create your views here.
def index(req):
    pet = Pet.objects.all()
    context = {}
    context["pet"] = pet
    return render(req, "index.html", context)


def petDetails(req, pid):
    pet = Pet.objects.get(pet_id=pid)
    context = {}
    context["pet"] = pet
    return render(req, "petDetail.html", context)


def viewCart(req):
    if req.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=req.user)
    else:
        cart_item = CartItem.objects.filter(user=None)
        messages.warning(req, "Log in to add to cart")
    context = {}
    context["items"] = cart_item
    total_price = 0
    for x in cart_item:
        print(x.pet.price, x.quantity)
        total_price += x.pet.price * x.quantity
        print(total_price)
    context["total"] = total_price
    length = len(cart_item)
    context["length"] = length
    return render(req, "cart.html", context)


def addCart(req, pid):
    pet = Pet.objects.get(pet_id=pid)
    user = req.user if req.user.is_authenticated else None
    if user:
        cart_item, created = CartItem.objects.get_or_create(pet=pet, user=user)
    else:
        return redirect("/login")
    print(cart_item, created)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    return redirect("/viewCart")


def removeCart(req, pid):
    pet = Pet.objects.get(pet_id=pid)
    cart_item = CartItem.objects.filter(pet=pet, user=req.user)
    cart_item.delete()
    return redirect("/viewCart")


from django.db.models import Q


def search(req):
    query = req.POST["q"]
    print(f"Query is {query}")
    if not query:
        result = Pet.objects.all()
    else:
        result = Pet.objects.filter(
            Q(pet_name__icontains=query)
            | Q(category__icontains=query)
            | Q(price__icontains=query)
        )
    return render(req, "search.html", {"results": result, "query": query})


def range(req):
    if req.method == "GET":
        return redirect("/")
    else:
        min = req.POST["min"]
        max = req.POST["max"]
        if min != "" and max != "" and min is not None and max is not None:
            queryset = Pet.pet.get_price_range(min, max)
            context = {}
            context["pet"] = queryset
            return render(req, "index.html", context)
        else:
            return redirect("/")


def catlist(req):
    if req.method == "GET":
        queryset = Pet.pet.catlist()
        context = {}
        context["pet"] = queryset
        return render(req, "index.html", context)


def doglist(req):
    if req.method == "GET":
        queryset = Pet.pet.doglist()
        context = {}
        context["pet"] = queryset
        return render(req, "index.html", context)


def birdlist(req):
    if req.method == "GET":
        queryset = Pet.pet.birdlist()
        context = {}
        context["pet"] = queryset
        return render(req, "index.html", context)


def fishlist(req):
    if req.method == "GET":
        queryset = Pet.pet.fishlist()
        context = {}
        context["pet"] = queryset
        return render(req, "index.html", context)


def priceOrder(req):
    queryset = Pet.objects.all().order_by("price")
    context = {}
    context["pet"] = queryset
    return render(req, "index.html", context)


def descpriceOrder(req):
    queryset = Pet.objects.all().order_by("-price")
    context = {}
    context["pet"] = queryset
    return render(req, "index.html", context)


def updateqty(req, uval, pid):
    pets = Pet.objects.get(pet_id=pid)
    a = CartItem.objects.filter(pet=pets)
    print(a)
    print(a[0])
    print(a[0].quantity)
    if uval == 1:
        temp = a[0].quantity + 1
        a.update(quantity=temp)
    else:
        temp = a[0].quantity - 1
        a.update(quantity=temp)
    return redirect("viewCart")


def viewOrder(req):
    cart_item = CartItem.objects.filter(user=req.user)
    print(cart_item)
    oid = random.randrange(1000, 9999)
    for x in cart_item:
        Order.objects.create(
            order_id=oid,
            product_id=x.pet.pet_id,
            quantity=x.quantity,
            user=req.user,
        )
        x.delete()
    orders = Order.objects.filter(user=req.user)
    context = {}
    context["items"] = orders
    total_price = 0
    for x in orders:
        print(x.pet.price, x.quantity)
        total_price += x.pet.price * x.quantity
        print(total_price)
    context["total"] = total_price
    length = len(orders)
    context["length"] = length
    return render(req, "viewOrder.html", context)


def register_user(req):
    form = CreateUserForm()
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, ("User created successfully"))
            return redirect("/")
        else:
            messages.error(req, ("Incorrect Username or Password Format"))
    context = {"form": form}
    return render(req, "register.html", context)


def login_user(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, ("Logged in Successfully"))
            return redirect("/")
        else:
            messages.error(req, ("There is error"))
            return redirect("/login")
    else:
        return render(req, "login.html")


def logout_user(req):
    logout(req)
    messages.success(req, ("Logged out Successfully"))
    return redirect("/")
