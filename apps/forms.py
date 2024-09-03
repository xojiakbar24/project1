from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password')

    def validate_password(self):
        password = self.cleaned_data['password']
        return make_password(password)