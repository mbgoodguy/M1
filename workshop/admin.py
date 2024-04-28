from django.contrib import admin

from workshop.models import Service, ServiceCategory


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'category')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ServiceCategory)
class AdminServiceCategory(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
