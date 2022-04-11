from django.urls import path
from api import views

urlpatterns = [
    path('book/', views.Bookview.as_view()),
    path('book/<int:id>', views.Booksdetails.as_view()),

]
