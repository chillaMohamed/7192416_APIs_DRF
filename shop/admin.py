from django.contrib import admin
from shop.models import Category, Product, Article


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'active')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'category_id', 'category', 'active')


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'product_id', 'product', 'category', 'active')

    @admin.display(description='Category')
    def category(self, obj):
        return obj.product.category


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
