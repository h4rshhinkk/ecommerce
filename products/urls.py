from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "web"


urlpatterns = [
    path("", views.IndexView.as_view(),name='index'),
    path('category',views.CategoryView.as_view(),name='category'),
    path('sub_category',views.SubCategoryView.as_view(),name='sub_category'),
    path('product',views.ProductView.as_view(),name='product'),
          
    #detailpages
    path('product/<slug:slug>/',views.ProductDetailView.as_view(), name='product_detail'),
]