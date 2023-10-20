
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include, path


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('web/', include("web.urls", namespace="web")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("main/", include("main.urls", namespace="main")),
    path("", include("products.urls", namespace="products")),

]

    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

)


admin.site.site_header = "Ecommerce Holidays Administration"
admin.site.site_title = "Ecommerce Holidays  Admin Portal"
admin.site.index_title = "Welcome to Ecommerce Holidays  Admin Portal"