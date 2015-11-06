from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('empleados.urls')),
    url(r'^$','empleados.views.logueo',name='/'),
    url(r'^logout$', 'empleados.views.Logout',name='logout'),
    url(r'^inicio$','empleados.views.index',name='inicio'),
    # url(r'^registrarse$','empleados.views.registrarse',name='registrarse'),
]
