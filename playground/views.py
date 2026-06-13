from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.
def say_hello(request):
  query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
  for pro in query_set:
    print(pro)
  return render(request,'hello.html') 