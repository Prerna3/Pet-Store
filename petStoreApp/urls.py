"""
URL configuration for petStoreProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("petDetails/<int:pid>", views.petDetails, name="petDetails"),
    path("viewCart/", views.viewCart, name="viewCart"),
    path("addCart/<int:pid>", views.addCart, name="addCart"),
    path("removeCart/<int:pid>", views.removeCart, name="removeCart"),
    path("search/", views.search, name="search"),
    path("range", views.range, name="range"),
    path("catlist", views.catlist, name="catlist"),
    path("doglist", views.doglist, name="doglist"),
    path("birdlist", views.birdlist, name="birdlist"),
    path("fishlist", views.fishlist, name="fishlist"),
    path("priceOrder", views.priceOrder, name="priceOrder"),
    path("descpriceOrder", views.descpriceOrder, name="descpriceOrder"),
    path("updateqty/<int:uval>/<int:pid>", views.updateqty, name="updateqty"),
    path("viewOrder", views.viewOrder, name="viewOrder"),
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("payment/", views.makePayment, name="payment"),
    path("myOrder/", views.myOrder, name="myOrder"),
    path("insertProduct/", views.insertProduct, name="insertProduct"),
]
