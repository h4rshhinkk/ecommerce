from django.shortcuts import render
from products.models  import Category,SubCategory,Product
from django.views.generic import ListView,DetailView
# Create your views here.


class IndexView(ListView):
    model = Category
    template_name = 'products/index.html'

class CategoryView(ListView):
    model = Category


class SubCategoryView(ListView):
    model = SubCategory


class ProductView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html' 
    context_object_name = 'product' 
