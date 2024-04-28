from django.urls import path
from workshop import views as ws_views

urlpatterns = [
    path("", ws_views.get_service_categories, name='get_service_categories_url'),
    path("<slug:category_slug>/<slug:service_slug>/", ws_views.service_detail, name='service_detail_url'),
    path("<slug:slug>/", ws_views.service_category_detail, name='service_category_detail_url')
]
