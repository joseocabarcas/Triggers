from django.contrib import admin
from .models import Auditoria
# Register your models here.

class AuditoriaAdmin(admin.ModelAdmin):
	list_display = ['operacion','usuario',]

admin.site.register(Auditoria, AuditoriaAdmin)