from rest_framework.viewsets import ReadOnlyModelViewSet
 
from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer
 
 
class CategoryViewSet(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
     
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)\
                                    .filter(category__active=True)\
                                    .order_by('-date_created')

        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset
    

class ArticleViewSet(ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
     
    def get_queryset(self):
        queryset = Article.objects.filter(active=True)\
                                    .filter(product__active=True)\
                                    .filter(product__category__active=True)\
                                    .order_by('-date_created')

        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)

        return queryset