from django.urls import path
from .views import producto , agregar_tienda, categoria
from django.conf import settings
from django.conf.urls.static import static
from carrito.views import carrito



urlpatterns = [
    path('',producto,name="producto"),
    path('carrito/',carrito,name='carrito'),
    path('producto/<int:producto_id>',agregar_tienda,name='add'),
    path('categoria/<int:categoria_id>/',categoria,name="categoria"),
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)