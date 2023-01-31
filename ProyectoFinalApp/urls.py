from django.urls import path
from .views import index, nosotros, login, pagina_vacia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('nosotros/',nosotros,name='nosotros'),
    path('login/',login, name='login'),
    path('vacia/',pagina_vacia, name='pagina_vacia')
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)