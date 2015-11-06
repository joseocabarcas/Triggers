from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .serializers import EmpleadoSerializer
from rest_framework import viewsets
from .models import Empleado

class EmpleadoViewSet(viewsets.ModelViewSet):
	queryset = Empleado.objects.all()
	serializer_class = EmpleadoSerializer


# Create your views here.

def logueo(request):
	if request.user.is_authenticated():
		return redirect('inicio')
	if request.method== "POST":
		login_form= LoginForm(request.POST)
		if login_form.is_valid():
			print "1"
			usuario= authenticate(username=login_form.cleaned_data['username'],password=
				login_form.cleaned_data['password'])
			if usuario is not None:
				if usuario.is_active:
					login(request,usuario)
					return redirect('inicio')
			else:
				return render(request,'login.html',{'login_form':login_form},context_instance=RequestContext(request))
		else:
			return render(request,'login.html',{'login_form':login_form},context_instance=RequestContext(request))

	login_form=LoginForm()
	return render(request,'login.html',{'login_form':login_form})

# def registrarse(request):
# 	return render(request,'registrarse.html')
@login_required(login_url='/')
def index(request):
	return render(request,'index.html')


@login_required(login_url='/')
def Logout(request):
	logout(request)
	request.session.flush()
	return redirect('/')