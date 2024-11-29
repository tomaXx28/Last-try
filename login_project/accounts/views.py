from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio
            else:
                # Manejar error de credenciales incorrectas
                return render(request, 'login.html', {'form': form, 'error': 'Usuario o contraseña incorrectos'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  # Asegúrate de tener esta plantilla