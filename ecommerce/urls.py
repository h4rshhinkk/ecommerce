
from django.contrib import admin
from django.urls import path
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls", namespace="web")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("main/", include("main.urls", namespace="main")),
    path("products/", include("products.urls", namespace="products")),

]
