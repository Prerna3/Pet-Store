from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pet
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddPet(ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"
