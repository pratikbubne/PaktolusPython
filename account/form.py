from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number', 'profession_type']
        field_order = ['username', 'email', 'password1', 'password2', 'mobile_number', 'profession_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user
