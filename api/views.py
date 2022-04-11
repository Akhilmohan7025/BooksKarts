from django.shortcuts import render
from owner.models import Books
from rest_framework.views import APIView
from api.serializer import Booksserilizers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class Bookview(APIView):
    def get(self, request, *args, **kwargs):
        book = Books.objects.all()
        serializers = Booksserilizers(book, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = Booksserilizers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Booksdetails(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        book = Books.objects.get(id=id)
        serializer = Booksserilizers(book)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        book = Books.objects.get(id=id)
        serializer = Booksserilizers(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
            id=kwargs.get("id")
            book=Books.objects.get(id=id)
            book.delete()
            return Response({"message","deleted"},status=status.HTTP_201_OK)


