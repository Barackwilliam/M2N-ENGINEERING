from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "M2N ENGINEERING"
admin.site.site_title = "M2N Engineering Admin"
admin.site.index_title = "Karibu M2N Engineering Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
