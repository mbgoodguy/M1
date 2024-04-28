from django.shortcuts import render, get_object_or_404

from workshop.models import Service, ServiceCategory


# Create your views here.

def home(request):
    return render(request, template_name="home.html")


def contacts(request):
    return render(request, template_name="contacts.html")


def service_category_detail(request, slug):
    service_category = get_object_or_404(ServiceCategory, slug=slug)
    related_services = service_category.services.all()

    return render(
        request,
        template_name='service_category_detail.html',
        context={
            'service_category': service_category,
            'related_services': related_services,
        }
    )


def service_detail(request, category_slug, service_slug):
    service = get_object_or_404(Service, slug=service_slug, category__slug=category_slug)
    return render(
        request,
        template_name='service_detail.html',
        context={'service': service}
    )


def get_service_categories(request):
    service_categories = ServiceCategory.objects.all()
    return render(
        request,
        template_name='service_categories_list.html',
        context={'service_categories': service_categories}
    )
