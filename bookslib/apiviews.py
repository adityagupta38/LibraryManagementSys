from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import Books

class BooksApi(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()