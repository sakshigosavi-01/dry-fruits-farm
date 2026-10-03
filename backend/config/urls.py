from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from store.views import products, cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='products'),
    path('cart/', cart, name='cart'),
    path('', include('store.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )