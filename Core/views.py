from django.shortcuts import render
from .models import Item ,OrderItem ,Order
from django.views.generic import ListView , DetailView 


# Create your views here.
def products(request):
    context ={
      'items':Item.objects.all()
    }
    return render(request, 'Core/products.html',context )


class HomeView(ListView):
  model = Item
  template_name = 'Core/index.html'

class ItemDetailView(DetailView):
  model = Item
  template_name='Core/products.html'