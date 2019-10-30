from django.urls import path, include

from . import views
app_name = 'portfolio'
urlpatterns= [
    path('', views.PortfolioListView.as_view(), name='index'),
    path('<slug:slug>', views.PortfolioDetailView , name='detail')
]