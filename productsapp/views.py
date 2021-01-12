from django.shortcuts import render
from django.views.generic import ListView, DetailView
from productsapp.models import Category, Product, ProductImage


class CategoryProducts(ListView):
    model = Product
    template_name = 'productsapp/category.html'

    def get_queryset(self):
        slug = self.kwargs.get('category_slug')
        products = Product.objects.filter(category__slug=slug)
        return products


class DetailProduct(DetailView):
    model = Product
    template_name = 'productsapp/product.html'
    context_object_name = 'product'

    # def get_object(self):
    #     slug = self.kwargs.get('product_slug')
    #     product = Product.objects.get(slug=slug)
    #     return product
