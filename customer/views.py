from django.shortcuts import render, redirect
from customer.forms import FeedbackForm
from django.views.generic import View, ListView, CreateView, UpdateView,TemplateView
from owner.models import Books
from customer.forms import UsersignupForm, userloginform, orderform, Profileform
from django.contrib.auth import authenticate, logout, login
from django.utils.decorators import method_decorator
from customer.decorators import sign_in_required
from customer.models import Carts, My_orders, Profile
from django.db.models import Sum
from django.urls import reverse_lazy


# Create your views here
@method_decorator(sign_in_required, name='dispatch')
class Customerhome(View):
    def get(self, request, *args, **kwargs):
        home = Books.objects.all()
        context = {"home": home}
        return render(request, "home.html", context)


class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedbackForm
        context = {'form': form}
        return render(request, "Feedback.html", context)
    # def post(self,request):


class signup(View):
    def get(self, request, *args, **kwargs):
        sign = UsersignupForm()
        context = {"signup": sign}
        return render(request, "signup.html", context)

    def post(self, request):
        signin = UsersignupForm(request.POST)
        if signin.is_valid():
            signin.save()
            print("user created")
            return render(request, "login.html")
        else:
            context = {"signup": signin}
            return render(request, "signup.html", context)


class log_in(View):
    def get(self, request, *args, **kwargs):
        log = userloginform()
        context = {"login": log}
        return render(request, "login.html", context)

    def post(self, request):
        log = userloginform(request.POST)
        if log.is_valid():
            username = log.cleaned_data.get("username")
            password = log.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("listbooks")
                else:
                    return redirect("homepage")
            else:
                context = {"login": login}
                return render(request, "login.html", context)
        else:
            context = {"login": login}
            return render(request, "login.html", context)


def signout(request):
    logout(request)
    return redirect("login")


class Add_to_cart(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        book = Books.objects.get(id=id)
        user = request.user
        cart = Carts(user=user, item=book)
        cart.save()
        print("successfully added to cart")
        return redirect("homepage")


class Cart_views(ListView):
    model = Carts
    template_name = "carts_items.html"
    context_object_name = "items"

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)

    def get(self, *args, **kwargs):
        logged_user = self.model.objects.filter(user=self.request.user, status="incart")
        total_sum = logged_user.aggregate(Sum("item__price"))
        total = total_sum["item__price__sum"]

        context = {"items": logged_user, "total": total}
        return render(self.request, self.template_name, context)


class Remove(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        remove = Carts.objects.get(id=id)
        remove.status = "cancel"
        remove.save()
        return redirect("cartview")


class My_orders_view(CreateView):
    model = My_orders
    template_name = "customerorders.html"
    form_class = orderform

    def post(self, request, *args, **kwargs):
        p_id = kwargs.get("p_id")
        c_id = kwargs.get("c_id")
        form = orderform(request.POST)
        if form.is_valid():
            book = Books.objects.get(id=p_id)
            cart = Carts.objects.get(id=c_id)
            user = request.user
            address = form.cleaned_data.get("address")
            order = My_orders(user=user, item=book, address=address)
            order.save()
            cart.status = "order_placed"
            cart.save()
            return redirect("homepage")


class Orderview(ListView):
    model = My_orders
    template_name = "orderviews.html"
    context_object_name = "orders"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="cancel")


class Ordercancel(View):
    def get(self, request, *args, **kwargs):
        o_id = kwargs.get("o_id")
        remove = My_orders.objects.get(id=o_id)
        remove.status = "cancel"
        remove.save()
        return redirect("orderview")


class Profileview(CreateView):
    model = Profile
    template_name = "profileview.html"
    form_class = Profileform
    def post(self, request):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            return redirect("homepage")
        else:
            return render(request, self.template_name, {"form": form})

class viewmyprofile(TemplateView):
    template_name = "myprofile.html"
