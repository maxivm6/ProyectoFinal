from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'carrito'

urlpatterns = [
    path('',carrito,name="carrito"),
    path('agregar/<int:producto_id>',agregar,name='agregar'),
    path('eliminar/<int:producto_id>',eliminar,name='eliminar'),
    path('restar/<int:producto_id>',restar,name='restar'),
    path('limpiar/',limpiar,name='limpiar')
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)