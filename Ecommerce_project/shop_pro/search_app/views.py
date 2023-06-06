from django.shortcuts import render
from shop_app.models import product
from django.db.models import Q


# Create your views here.
def search_result(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = product.objects.all().filter(Q(pro_name__contains=query) | Q(des__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
