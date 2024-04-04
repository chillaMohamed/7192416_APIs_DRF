from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
 
from shop.models import Category
from shop.serializers import CategorySerializer
 
 
class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()