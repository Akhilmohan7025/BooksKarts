from rest_framework.serializers import ModelSerializer
from owner.models import Books

class Booksserilizers(ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"