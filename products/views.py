from django.shortcuts import render
from products.models  import Category,SubCategory,Product
from django.views.generic import ListView
# Create your views here.

class CategoryView(ListView):
    model = Category
    

class SubCategoryView(ListView):
    model = SubCategory


class ProductView(ListView):
    model = Product

