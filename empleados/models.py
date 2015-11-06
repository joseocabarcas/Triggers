from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

# class UsuarioManager(BaseUserManager, models.Manager):

# 	def _create_user(self,username,nombre,apellido,password,is_staff,is_superuser, **extra_fields):
# 		user = self.model(username = username, nombre=nombre,
# 			apellido=apellido,is_active= True, is_staff= is_staff, is_superuser= is_superuser,
# 			**extra_fields)
# 		user.set_password(password)
# 		user.save(using = self._db)
# 		return user

# 	def _create_superuser(self,username,password,is_staff,is_superuser, **extra_fields):
# 		user = self.model(username = username, is_active= True, is_staff= is_staff, is_superuser= is_superuser,
# 			**extra_fields)
# 		user.set_password(password)
# 		user.save(using = self._db)
# 		return user

# 	def create_user(self, username, nombre,apellido ,password=None,**extra_fields):
# 		return self._create_user(username,nombre,apellido,password,False,False, **extra_fields)

# 	def create_superuser(self, username,  password=None,**extra_fields):
# 		return self._create_superuser(username,password,True,True, **extra_fields)

# class Usuario(AbstractBaseUser, PermissionsMixin):
# 	nombre  = models.CharField(max_length=100)
# 	apellido  = models.CharField(max_length=100)
# 	username = models.CharField(max_length=100,unique=True)

# 	objects = UsuarioManager()

# 	is_active = models.BooleanField(default=True)
# 	is_staff = models.BooleanField(default=False)

# 	USERNAME_FIELD ='username'

# 	def get_short_name(self):
# 		return self.username

# 	def get_name_complete():
# 		return self.nombre +' '+self.apellido


class Empleado(models.Model):
    """
    Description: Model Description
    """
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)
    empresa = models.CharField(max_length=50)
    salario = models.PositiveIntegerField()
    usuario = models.CharField(max_length=50)

