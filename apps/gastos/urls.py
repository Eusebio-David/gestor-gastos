from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos, name='index'),
    path('gastos/', views.GastoListView.as_view(), name='lista_de_gastos'),
]
