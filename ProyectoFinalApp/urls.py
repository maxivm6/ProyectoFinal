from django.urls import path
from .views import index, nosotros, login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('nosotros/',nosotros,name='nosotros'),
    path('login/',login, name='login'),
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)