from django.urls import path, include

from . import views
app_name = 'price'
urlpatterns= [
    path('', views.PriceListView.as_view(), name='index'),
   
    path('<slug:slug>', views.PriceDetailView , name='detail')
]