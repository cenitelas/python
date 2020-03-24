from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LogonForm, SignUpForm, SearchForm, ProfileForm, MessageForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.db.models.functions import Concat
from django.db.models import Value
import os
from .models import Message


def index(request):
    if request.user.is_anonymous:
        return redirect(main)
    return redirect(logon)


def logon(request):
    if not request.user.is_anonymous:
        return redirect(main)
    if request.method == 'POST':
        form = LogonForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(username=form.data['login'], password=form.data['password'])
                if user.is_active:
                    login(request, user)
                    return redirect(main)
                else:
                    return HttpResponse('Ваш аккаунт не активирован')
            except Exception as e:
                return render(request, 'logon.html', {'form': form, 'error': 'Данного аккаунта не существует'})
    else:
        form = LogonForm()

    return render(request, 'logon.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Social Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return HttpResponse('К вам на почту отправлено письмо для активации аккаунта')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect(main)
    else:
        return HttpResponse('Ошибка активации аккаунта')


def main(request):
    if request.user.is_anonymous:
        return redirect(logon)
    request.user.profile.photo = str(request.user.profile.photo).replace('polls', '')
    return render(request, 'profile.html', {'profile': request.user})


def send_message(request):
    if request.user.is_anonymous:
        return redirect(logon)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            try:
                message = Message()
                message.sender = request.user
                message.message = form.data['message']
                message.recipient = User.objects.get(id=form.data["recipient_id"])
                message.save()
                return HttpResponse("Сообщение отправлено")
            except Exception as e:
                return HttpResponse("Ошибка отправки сообщения")
    return HttpResponse("Ошибка отправки сообщения")


def get_messages(request, sender_id: int):
    if request.user.is_anonymous:
        return redirect(logon)
    sender = User.objects.get(id=sender_id)
    sender.profile.photo = str(sender.profile.photo).replace('polls', '')
    chat = {sender: []}
    for mes in Message.objects.filter(recipient=request.user):
        if mes.sender == sender:
            chat[sender].append(mes)

    for mes in Message.objects.filter(sender=request.user):
        if mes.recipient == sender:
            chat[sender].append(mes)

    chat[sender].sort(key=lambda x: x.date, reverse=False)
    return render(request, 'messages.html', {'chat': chat, 'friend': sender})


def get_chat(request, sender_id: int):
    if request.user.is_anonymous:
        return redirect(logon)
    sender = User.objects.get(id=sender_id)

    return render(request, 'chat.html', {'friend': sender})


def get_chats(request):
    if request.user.is_anonymous:
        return redirect(logon)
    chats = {}
    for mes in Message.objects.filter(recipient=request.user):
        if mes.sender not in chats.keys():
            sender = mes.sender
            sender.profile.photo = str(sender.profile.photo).replace('polls', '')
            chats[sender] = []

    for mes in Message.objects.filter(sender=request.user):
        if mes.recipient not in chats.keys():
            recipient = mes.recipient
            recipient.profile.photo = str(recipient.profile.photo).replace('polls', '')
            chats[recipient] = []

    return render(request, 'chats.html', {'chats': chats})


def profile(request, profile_id: int):
    if request.user.is_anonymous:
        return redirect(logon)
    try:
        user = User.objects.get(id=profile_id)
        user.profile.photo = str(user.profile.photo).replace('polls', '')
        return render(request, 'profile.html', {'profile': user})
    except Exception as e:
        return redirect(logon)


def search(request):
    if request.user.is_anonymous:
        return redirect(logon)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            try:
                all_users = User.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
                users = all_users.filter(fullname__icontains=form.data['search'])
                return render(request, 'search_result.html', {'profiles': users})
            except Exception as e:
                return HttpResponse("Пользователь не найден")
    return HttpResponse("Пользователь не найден")


def change_profile(request):
    if request.user.is_anonymous:
        return redirect(logon)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            if request.FILES:
                if user.profile.photo:
                    os.remove(str(user.profile.photo))
                user.profile.photo = request.FILES['photo']
            user.first_name = form.data['user_first_name']
            user.last_name = form.data['user_last_name']
            if form.data['birth_date']:
                user.profile.birth_date = form.data['birth_date']
            user.save()
            return redirect(main)
        else:
            return redirect(main)
    else:
        form = ProfileForm()
        return render(request, 'change_profile.html', {'form': form})
