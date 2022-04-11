from django.urls import path
from customer import views

urlpatterns = [
    # path("feedback/form", views.FeedbackForm.as_view(), name="feedback"),
    # path("books/all", views.Book_list.as_view(), name="listbooks"),
    # path("books/<int:id>", views.Book_details.as_view(), name="bookdetails"),
    path("home", views.Customerhome.as_view(), name="homepage"),
    path("account/signup", views.signup.as_view(), name="signup"),
    path("", views.log_in.as_view(), name="login"),
    path("account/logout", views.signout, name="logout"),
    path("customer/addtocart/<int:id>", views.Add_to_cart.as_view(), name="addtocart"),
    path("customer/viewcartsitem", views.Cart_views.as_view(), name="cartview"),
    path("customer/remove/carts/<int:id>", views.Remove.as_view(), name="removecartsitem"),
    path("customer/placeorder/<int:p_id>/<int:c_id>", views.My_orders_view.as_view(), name="orderplaced"),
    path("customer/orderviews", views.Orderview.as_view(), name="orderview"),
    path("customer/ordercancel/<int:o_id>", views.Ordercancel.as_view(), name="ordercancel"),
    path("customer/userprofile", views.Profileview.as_view(), name="profileview"),
    path("customer/myprofile", views.viewmyprofile.as_view(), name="viewmyprofile")

]
