from django.urls import path
from . import views


"""
módulo de urls de la app gastos
Este módulo define las rutas de la aplicación de gestión de gastos.
Cada ruta esta asociada a una vista específica que maneja las operaciones relacionadas con los gastos, como listar, crear, editar y eliminar gastos.
"""
urlpatterns = [
    path("", views.Inicio, name='inicio'),
    path('gastos/', views.ListaDeGastos.as_view(), name='lista_de_gastos'),
    path('<int:pk>/detalle', views.GastoEditarDetalle.as_view(), name='gasto_detalle'),
    path('crear/', views.CrearGasto.as_view(), name='crear_gasto' ),
    path('eliminar/<int:pk>', views.EliminarGasto.as_view(), name='eliminar_gasto')
]
