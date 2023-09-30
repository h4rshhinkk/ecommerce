from django.urls import path
from . import views

app_name = "web"


urlpatterns = [
    path('category',views.CategoryView.as_view(),name='category'),
    path('sub_category',views.SubCategoryView.as_view(),name='sub_category'),
    path('product',views.ProductView.as_view(),name='product'),
      
]