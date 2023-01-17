from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import eventos


urlpatterns = [
    path('',eventos,name="eventos")  
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)