from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class RegistrForm(forms.Form):
    username = forms.CharField(label='Логин')
    name = forms.CharField(max_length=20, label='Имя')
    surname = forms.CharField(max_length=20, label='Фамилия')
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_1 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='This field is required')
    phone_number = forms.CharField(max_length=20, label='Номер телефона')


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'email', 'phone_number', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('name', 'surname', 'email', 'phone_number', 'username')





