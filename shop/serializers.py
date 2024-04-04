from rest_framework.serializers import ModelSerializer

from shop.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'active','date_created']
        read_only_fields = ['name']