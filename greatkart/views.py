#  from django.http import HttpResponse
from django.shortcuts import render
import datetime
from store.models import Product


def home(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse('HomePage')
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products
    }
    return render(request, 'home.html', context)
