from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from similarapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.media_upload, name='media_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
