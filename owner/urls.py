from django.urls import path
from owner import views

urlpatterns = [
    path("books/all", views.Book_list.as_view(), name="listbooks"),
    path("books/<int:id>", views.Book_details.as_view(), name="bookdetails"),
    path("books/add", views.Book_add.as_view(), name="addbooks"),
    path("books/edit/<int:id>", views.Book_edit.as_view(), name="editbooks"),
    path("books/del/<int:id>", views.Book_delete.as_view(), name="deletebooks"),
    path("dashboard", views.Ownerdashbord.as_view(), name="ownerdashboard"),
    path("dashboard/viewbook/<int:id>", views.Dashview.as_view(), name="viewdashbord"),
    path("dashboard/orderprocess/<int:id>", views.Orderprocess.as_view(), name="orderprocess"),

]

