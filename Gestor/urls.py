"""
URL configuration for Gestor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps.usuarios.views import ReenviarPasswordResetEmailView, MiPasswordResetView

#URLs del proyecto y app Gastos
urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("", include("apps.gastos.urls")),
    path("usuario/", include("apps.usuarios.urls")),
    #Path para la autenticacion 
    # Sobrescribir la vista para password reset (para guardar el email en sesión)
    path('accounts/password_reset/', MiPasswordResetView.as_view(), name='password_reset'),

    #  Ruta para reenviar email
    path("accounts/resend-reset/", ReenviarPasswordResetEmailView.as_view(), name="resend_password_reset"),

    # Incluir el resto de las rutas auth por defecto de Django
    path('accounts/', include('django.contrib.auth.urls')),

    #Incluir rutas de contacto
    path("", include('apps.contacto.urls')),

    #incluir rutas para preguntas frecuentes
    path("", include('apps.preguntas.urls')),

    #ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #blog
    path('', include('apps.Blog.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  