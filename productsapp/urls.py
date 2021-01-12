from django.urls import path
from productsapp.views import CategoryProducts, DetailProduct

app_name = 'products'

urlpatterns = [
    path('<category_slug>/', CategoryProducts.as_view()),
    path('<product_slug>/', DetailProduct.as_view()),
]
