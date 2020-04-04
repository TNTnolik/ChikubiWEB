from django.contrib import admin
from django.urls import path, include
from .settings import DEBUG, STATIC_URL, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', include("anime.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)