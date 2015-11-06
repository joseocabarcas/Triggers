
from django.conf.urls import include, url
from rest_framework import routers
from .views import EmpleadoViewSet

router =routers.SimpleRouter()
router.register(r'empleados',EmpleadoViewSet)
urlpatterns = [
    url(r'^api/', include(router.urls)),    
]
