from django.contrib import admin
from .models import Category,Product,Brand,ProductLine,ProductImage,Attribute,AttributeValue,ProductLineAttributeValue
# Register your models here.

class ProductInline(admin.TabularInline):
    model = ProductLine
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]

admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductLineAttributeValue)
admin.site.register(ProductLine)



