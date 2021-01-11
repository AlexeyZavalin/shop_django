from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя категории')
    slug = models.SlugField()
    is_published = models.BooleanField(default=True, verbose_name='Категория опубликована')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя товара', db_index=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    description = models.TextField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    stock = models.IntegerField(null=True, blank=True)
    is_weight = models.BooleanField(default=False, verbose_name='Весовой товар')
    is_published = models.BooleanField(default=True, verbose_name='Товар опубликован')
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        ordering = ['price', 'title']


class ProductImage(models.Model):
    image = models.ImageField(upload_to='media/products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
