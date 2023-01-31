from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import eventos, mostrar_evento


urlpatterns = [
    path('',eventos,name="eventos"),
    path('mostrar_evento/<int:post_id>',mostrar_evento,name="mostrar_evento"),  
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)