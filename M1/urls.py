from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from workshop import views as ws_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", ws_views.home, name='home'),
    path("contacts/", ws_views.contacts, name='contacts'),
    path('services/', include('workshop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
