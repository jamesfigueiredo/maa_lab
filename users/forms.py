from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff', 'is_superuser']
        #fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'type':'password', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
        }
        labels = {
            'username': 'Nome',
            'password': 'Senha',
            'email': 'E-mail',
        }