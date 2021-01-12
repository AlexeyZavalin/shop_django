from django.urls import path
from productsapp.views import CategoryProducts, DetailProduct

app_name = 'products'

urlpatterns = [
    path('<slug:category_slug>/', CategoryProducts.as_view()),
    path('<slug:category_slug>/<slug:product_slug>/', DetailProduct.as_view()),
]
