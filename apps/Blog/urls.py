from django.urls import path
from . import views
urlpatterns = [
   path('posts/', views.PostLista, name='lista_post' ),
   path('posts/detalle/<int:pk>/<slug:slug>/', views.PostDetalle.as_view(), name='post_detalle')
]
