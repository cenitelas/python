from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LogonForm, SignUpForm
from django.contrib.auth import login, authenticate


def index(request):
    return HttpResponse('')


def logon(request):
    if request.method == 'POST':
        form = LogonForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['login'], password=form.data['password'])
            login(request, user)
            return redirect(main)
    else:
        form = LogonForm()

    return render(request, 'logon.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(main)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def main(request):
    return render(request, 'main.html')
