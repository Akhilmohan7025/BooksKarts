from django.contrib import admin
from customer.models import Carts
from owner.models import Books
# Register your models here.
admin.site.register(Carts)
admin.site.register(Books)