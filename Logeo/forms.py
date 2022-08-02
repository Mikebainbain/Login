from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Tabla de usuarios por default qie ofrece django

class UserRegisterForm(UserCreationForm): # UserRegisterForm heredar todas las funcionalidades que tiene UserCreationForm
    # decir que campos se desean
    email = forms.EmailField()
    password1 = forms.CharField(label ='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label ='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields } # Para remover lso textos de ayuda que nos muestra el formulario de register de  django 

