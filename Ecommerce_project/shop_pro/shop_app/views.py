from .models import Category, product
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def all_category(request, cat_slug=None):
    cat_page = None
    cat_product_list = None
    if cat_slug!=None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        cat_product_list = product.objects.all().filter(category=cat_page, available=True)
    else:
        cat_product_list = product.objects.all().filter(available=True)
    paginator = Paginator(cat_product_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': cat_page, 'products': products})


def pro_detail(request, cat_slug, product_slug):
    try:
        products = product.objects.get(category__slug=cat_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': products})
