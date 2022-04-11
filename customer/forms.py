from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from customer.models import My_orders, Profile


class FeedbackForm(forms.Form):
    product = forms.CharField()
    feedback = forms.CharField()


class UsersignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        # widget={
        #     'username':forms.TextInput(attrs={"class":"form-control"}),
        #     'first_name': forms.TextInput(attrs={"class": "form-control"}),
        #     'last_name': forms.TextInput(attrs={"class": "form-control"}),
        #     'email': forms.EmailField(attrs={"class": "form-control"}),
        #
        #
        # }


class userloginform(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput())


class orderform(forms.ModelForm):
    class Meta:
        model = My_orders
        fields = ["address"]
        widgets = {
            'address': forms.Textarea(attrs={"class": "form-control"}),
        }


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic", "address", "phone_number"]
        widgets = {
            'profile_pic': forms.FileInput(attrs={"class": "form-control"}),
            'address': forms.Textarea(attrs={"class": "form-control"}),
            'phone_number': forms.NumberInput(attrs={"class": "form-control"})
        }
