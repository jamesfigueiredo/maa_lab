from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm


@login_required
def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Não salva diretamente no banco
            user.set_password(form.cleaned_data['password']) # Criptografa a senha
            user.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('register')
        else:
            messages.error(request, "Erro ao criar o usuário. Verifique os dados.")
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})

#@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#@login_required
def suppliers_view(request):
    if request.method == 'GET':
        return render(request, 'suppliers.html')

#@login_required
def brands_view(request):
    if request.method == 'GET':
        return render(request, 'brands.html')

#@login_required    
def products_view(request):
    if request.method == 'GET':
        return render(request, 'products.html')

#@login_required
def list_users(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "list_users.html", {"users": users})