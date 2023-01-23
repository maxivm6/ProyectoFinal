from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import loguear, Registro, cerrar_sesion


urlpatterns = [
    path('',loguear,name="login"),
    path('registro/',Registro.as_view(),name="Registro"),
    path('cerrar_sesion/', cerrar_sesion, name="Logout")  
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)