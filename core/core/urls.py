
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('accounts/', include('accounts.urls',namespace="accounts")),
    path('page-admin/', include('pageadmin.urls',namespace="pageadmin")),
    path('page-projeto/', include('projeto.urls',namespace="projetos"),),
    path('page-socio/', include('socios.urls',namespace="socios"),),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)