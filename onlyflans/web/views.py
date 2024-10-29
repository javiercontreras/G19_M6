from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseForbidden
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Flan
# Create your views here.
def indice(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request,'index.html',{'flanes':flanes})

def acerca(request):
    return render(request,'about.html',{})

def bienvenido(request):
    return render(request,'welcome.html',{})

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect('home')
            except:
                return HttpResponse("El usuario ya existe")
        return HttpResponse("Las contraseñas no coinciden")

def sign_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm,'error':"El usuario o contraseña son incorrectos"})
        else:
            login(request,user)
            return redirect('/')