from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empleado