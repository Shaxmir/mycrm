from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.catalog.urls', namespace='catalog')),
    path('core/', include('apps.core.urls')),
    path('deals/', include('apps.deals.urls')),
    path('documents/', include('apps.documents.urls')),
    path('logistics/', include('apps.logistics.urls', namespace='logistics')),
    path('users/', include('apps.users.urls')),
    path('warehouses/', include('apps.warehouse.urls', namespace='warehouse')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
