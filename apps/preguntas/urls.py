from django.urls import path
from . import views
urlpatterns = [
    path('preguntas/lista', views.ListaDePreguntas, name='lista_de_preguntas'),
    path('preguntas/<int:pk>/', views.PreguntasFrecuentesDetalle.as_view(), name='pregunta_detalle')
]
