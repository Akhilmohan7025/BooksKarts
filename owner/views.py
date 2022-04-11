from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, DetailView, DeleteView, CreateView
from owner.models import Books
from owner.forms import Bookform,OrderProcessForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from customer.decorators import owner_sign_in_required
from customer.views import My_orders
from django.core.mail import send_mail


# Create your views here.

@method_decorator(owner_sign_in_required, name='dispatch')
class Book_list(ListView):
    model = Books
    context_object_name = "book"
    template_name = "view_all_bks.html"

    # def get(self, request, *args, **kwargs):
    #     book = Books.objects.all()
    #     context = {"book": book}
    #     return render(request, "view_all_bks.html", context)


@method_decorator(owner_sign_in_required, name='dispatch')
class Book_add(CreateView):
    model = Books
    form_class = Bookform
    context_object_name = 'item'
    template_name = "add_book.html"

    # def get(self, request, *args, **kwargs):
    #     form = Bookform()
    #     context = {'item': form}
    #     return render(request, "add_book.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = Bookform(request.POST, files=request.FILES)
    #     # print(request.POST)
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         book_name = form.cleaned_data.get("book_name")
    #         author = form.cleaned_data.get("author")
    #         price = form.cleaned_data.get("price")
    #         copies = form.cleaned_data.get("copies")
    #         book = Books(book_name=book_name, author=author, price=price, copies=copies)
    #         book.save()
    #         messages.success(request,"successfully book added")
    #         return redirect("addbooks")
    #     else:
    #         context = {'item': form}
    #         messages.error(request="booking adding failed")
    #         return render(request,"add_book.html",context)


@method_decorator(owner_sign_in_required, name='dispatch')
class Book_details(DetailView):
    model = Books
    context_object_name = "detail"
    pk_url_kwarg = 'id'
    template_name = "book_dtl.html"
    success_url = reverse_lazy("listbooks")

    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     detail = Books.objects.get(id=id)
    #     context = {"detail": detail}
    #     return render(request, "book_dtl.html", context)


@method_decorator(owner_sign_in_required, name='dispatch')
class Book_edit(UpdateView):
    model = Books
    form_class = Bookform
    context_object_name = "edit"
    pk_url_kwarg = 'id'
    template_name = "book_edit.html"
    success_url = reverse_lazy("listbooks")

    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     edit = Books.objects.get(id=id)
    #     # dict={"book_name":edit.book_name,
    #     #       "author":edit.author,
    #     #       "price":edit.price,
    #     #       "copies":edit.copies
    #     #       }
    #     form = Bookform(instance=edit)
    #     context = {"edit": form}
    #     return render(request, "book_edit.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     edit = Books.objects.get(id=id)
    #     dict = Bookform(request.POST, instance=edit, files=request.FILES)
    #     if dict.is_valid():
    #         dict.save()
    #         return redirect("listbooks")


@method_decorator(owner_sign_in_required, name='dispatch')
class Book_delete(DeleteView):
    model = Books
    pk_url_kwarg = 'id'
    template_name = "delete_books.html"
    success_url = reverse_lazy("listbooks")
    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     dele = Books.objects.get(id=id)
    #     dele.delete()
    #     return redirect("listbooks")





class Ownerdashbord(ListView):
    model = My_orders
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        new_order = My_orders.objects.filter(status="order_placed")
        context = {"odr": new_order}
        return render(request, "dashboard.html", context)


class Dashview(DetailView):
    model = My_orders
    context_object_name = "detail"

    pk_url_kwarg = 'id'
    template_name = "viewbook.html"


class Orderprocess(UpdateView):
    model = My_orders
    template_name = "orderprocess.html"
    pk_url_kwarg = "id"
    form_class = OrderProcessForm
    success_url = reverse_lazy("ownerdashboard")

    def form_valid(self, form):
        self.object=form.save()
        excepted_delivery_date=form.cleaned_data.get("excepted_delivery_date")
        send_mail(
            'Successfully Book ordered',
            'Your order will be delivered on.'+str(excepted_delivery_date),
            'akhilmohan04869@gmail.com',
            ['rinucherian2000@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)
