from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos, name='index')
]
