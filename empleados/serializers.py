from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empleado
		exclude = ('usuario',)


	def create(self, validated_data):
		request = self.context.get('request', None)
		empleado = Empleado.objects.create(
		nombres    =validated_data['nombres'], # HERE
		apellidos       =validated_data['apellidos'],
		cedula    =validated_data['cedula'],
		empresa  =validated_data['empresa'], 
		salario   =validated_data['salario'],
		usuario      = request.user.id,
		)
		return empleado