from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mi_perfil, editar_perfil


urlpatterns = [
    path('',mi_perfil,name="mi_perfil"),
    path('editar/',editar_perfil,name="editar_perfil")  
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)