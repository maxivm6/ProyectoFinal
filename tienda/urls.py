from django.urls import path
from .views import producto , agregar_tienda, categoria
from django.conf import settings
from django.conf.urls.static import static
from carrito.views import carrito



urlpatterns = [
    path('',producto,name="producto"),
    path('carrito/',carrito,name='carrito'),
    path('producto/<int:producto_id>',agregar_tienda,name='add'),
    path('categoria/<categoria_id>/',categoria,name="Categoria"),
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)