from django.contrib import admin
from .models import Category, product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name', 'slug']
    prepopulated_fields = {'slug': ('cat_name',)}
admin.site.register(Category, AdminCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','pro_name', 'price', 'stock', 'available', 'created', 'update']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('pro_name',)}
    list_per_page = 15
admin.site.register(product, ProductAdmin)
