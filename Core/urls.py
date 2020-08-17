from django.urls import path
from .views import (
  HomeView,
  ItemDetailView,
  products
)

app_name = 'Core'

urlpatterns = [
  
    path('', HomeView.as_view(), name='home'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),
  #  path('about/', views.about, na
  #  path('about/', views.about, name='blog-about'),
   
]