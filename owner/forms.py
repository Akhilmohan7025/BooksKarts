from django import forms
from django.forms import ModelForm
from owner.models import Books
from customer.views import My_orders


class Bookform(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "images": forms.FileInput(attrs={"class": "form-control"}),
        }

# class Bookform(forms.Form):
#     book_name=forms.CharField()
#     author=forms.CharField()
#     price=forms.CharField()
#     copies=forms.CharField()


class OrderProcessForm(ModelForm):
    class Meta:
        model = My_orders
        fields = ["status", "excepted_delivery_date"]

        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "excepted_delivery_date": forms.DateInput(attrs={"class": "form-control","type":"date"})
        }
