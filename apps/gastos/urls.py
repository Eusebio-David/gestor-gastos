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
    path('gasto/<int:pk>/detalle', views.GastoEditarDetalle.as_view(), name='gasto_detalle'),
    path('creargasto/', views.CrearGasto.as_view(), name='crear_gasto' ),
    path('eliminar/<int:pk>', views.EliminarGasto.as_view(), name='eliminar_gasto'),

    #urls para crear presupuesto 
    path('crearpresupuesto/', views.CrearPresupuesto.as_view(), name='crear_presupuesto'),
    path('presupuesto/<int:pk>/detalle', views.PresupuestoDetalle.as_view(), name='detalle_presupuesto'),
    path('eliminarpresupuesto/<int:pk>/delete', views.PresupuestoEliminar.as_view(), name='eliminar_presupuesto'),
    path('editarpresupuesto/<int:pk>/', views.PresupuestoEditar.as_view(),name='editar_presupuesto'),

    #urls para categoria
    path("categoria/crear/", views.CrearCategoria.as_view(), name='crear_categoria'),
    path("categoria/lista/", views.ListaDeCategorias.as_view(), name='lista_de_categoria')
]
