from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_name = Phone.objects.all()
    sort_name = request.GET.get('sort')
    if sort_name == 'name':
        phone_name = Phone.objects.order_by('name')
    if sort_name == 'min_price':
        phone_name = Phone.objects.order_by('price')
    if sort_name == 'max_price':
        phone_name = Phone.objects.order_by('-price')
    context = {'phones': phone_name}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_one = Phone.objects.get(slug=slug)
    context = {'phone': phone_one}
    return render(request, template, context)
