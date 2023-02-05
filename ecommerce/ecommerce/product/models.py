from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField


class ActiveManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active =True)

    def isactive(self):
        return self.get_queryset().filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    # objects = models.Manager() # default manager
    # isactive = ActiveManager() # custome manager

    objects = ActiveManager()  # default manager

    # isactive = ActiveManager() # custome manager

    def __str__(self) -> str:
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='attribute_value')

    def __str__(self) -> str:
        return f"{self.attribute_value}"


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=100)  # stock keeping units
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_line')
    attribute_values = models.ManyToManyField(
        AttributeValue, through="ProductLineAttributeValue")
    is_active = models.BooleanField(default=False)
    order = OrderField(blank=True, unique_for_field="product")

    def clean(self):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")

        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f' Price : {self.price} name PRoducr : {self.product.name}'


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        AttributeValue, on_delete=models.CASCADE, related_name='product_attribute_value_av')
    product_line = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name='product_attribute_value_pl')

    class Meta:
        unique_together = ('attribute_value', 'product_line')


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default="text.jpg")
    productline = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name='product_image')

    order = OrderField(blank=True, unique_for_field="productline")

    def clean(self):
        qs = ProductImage.objects.filter(productline=self.productline)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")

        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)


class ProductType(models.Model):
    name = models.CharField(max_length=100)


class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name='product_type_attribute_pt')
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='product_type_attribute_a')

    class Meta:
        unique_together = ('product_type', 'attribute')
