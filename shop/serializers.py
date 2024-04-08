from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product, Article


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created']


class CustomCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = CustomCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category','date_created']


class CustomProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category_id']


class ArticleSerializer(ModelSerializer):
    product = CustomProductSerializer()

    class Meta:
        model = Article
        fields = ['id', 'name', 'description', 'price', 'product', 'date_created']