from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogonForm(forms.Form):
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', max_length=100)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        error_messages = {
            'password1': "asdasd.",
            'password2': "asdasd.",
        }


class SearchForm(forms.Form):
    search = forms.CharField(label='search', max_length=100, required=True)


class ProfileForm(forms.Form):
    user_first_name = forms.CharField(max_length=30, help_text='Optional.')
    user_last_name = forms.CharField(max_length=30, help_text='Optional.')
    birth_date = forms.DateField(required=False)
    photo = forms.ImageField(required=False)


class MessageForm(forms.Form):
    sender_id = forms.HiddenInput()
    message = forms.CharField(max_length=200, required=True)

