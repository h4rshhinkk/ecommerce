from django.contrib import admin
from .models import Category,SubCategory,Product
# Register your models here.
# admin.site.register(Category)

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1  # Number of empty forms to display


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',) 
    prepopulated_fields = {"slug": ("category_name",)}
    inlines = [SubCategoryInline]  # Add the TabularInline for TourPlan


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('sub_category_name',) 
    prepopulated_fields = {"slug": ("sub_category_name",)}


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('product_name','price','description')
    prepopulated_fields = {"slug": ("product_name",)}


