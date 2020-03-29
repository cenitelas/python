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
import logging


log = logging.getLogger('social')


def index(request):
    log.info('Go to index',)
    return redirect(main)


def logon(request):
    log.info('logon show')
    if not request.user.is_anonymous:
        log.info('Logon user is not anonymous')
        return redirect(main)
    if request.method == 'POST':
        log.info('Logon request is post')
        form = LogonForm(request.POST)
        if form.is_valid():
            log.info('Logon form is valid')
            try:
                user = authenticate(username=form.data['login'], password=form.data['password'])
                if user.is_active:
                    log.info('Logon success sign')
                    login(request, user)
                    return redirect(main)
                else:
                    log.info('Logon account is not active')
                    return HttpResponse('Ваш аккаунт не активирован')
            except Exception as e:
                log.info('Logon account does not exist')
                return render(request, 'logon.html', {'form': form, 'error': 'Данного аккаунта не существует'})
    else:
        form = LogonForm()
    log.info('Logon request is get')
    return render(request, 'logon.html', {'form': form})


def signup(request):
    log.info('Sign up show')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        log.info('Sign up request is post')
        if form.is_valid():
            log.info('Sign up form valid')
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
            log.info('Sign up send activation page to user')
            return HttpResponse('К вам на почту отправлено письмо для активации аккаунта')
    else:
        form = SignUpForm()
    log.info('Sign up request is get')
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    log.info(f'{request.user.username} on logout')
    logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    log.info('Active user show')
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        log.info('Active user exist')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        log.info('Active does not user exist')
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        log.info('Active user success activation')
        return redirect(main)
    else:
        log.info('Active error user activation')
        return HttpResponse('Ошибка активации аккаунта')


def main(request):
    log.info('Main show')
    if request.user.is_anonymous:
        log.info('User is anonymous')
        return redirect(logon)
    log.info('User go to user profile')
    request.user.profile.photo = str(request.user.profile.photo).replace('polls', '')
    return render(request, 'profile.html', {'profile': request.user})


def send_message(request):
    log.info('Send message show')
    if request.user.is_anonymous:
        log.info('Send message user is anonymous')
        return redirect(logon)
    if request.method == 'POST':
        log.info('Send message request is post')
        form = MessageForm(request.POST)
        if form.is_valid():
            log.info('Send message form valid')
            try:
                message = Message()
                message.sender = request.user
                message.message = form.data['message']
                message.recipient = User.objects.get(id=form.data["recipient_id"])
                message.save()
                log.info('Send message message send success')
                return HttpResponse("Сообщение отправлено")
            except Exception as e:
                log.info('Send message error send message')
                return HttpResponse("Ошибка отправки сообщения")
    log.info('Send message error send message')
    return HttpResponse("Ошибка отправки сообщения")


def get_messages(request, sender_id: int):
    log.info('Get messages show')
    if request.user.is_anonymous:
        log.info('Get messages user is anonymous')
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
    log.info('Get messages send messages to users')
    return render(request, 'messages.html', {'chat': chat, 'friend': sender})


def get_chat(request, sender_id: int):
    if request.user.is_anonymous:
        log.info('Get chat user is anonymous')
        return redirect(logon)
    sender = User.objects.get(id=sender_id)
    log.info('Get chat show')
    return render(request, 'chat.html', {'friend': sender})


def get_chats(request):
    log.info('Get chats show')
    if request.user.is_anonymous:
        log.info('Get chats user is anonymous')
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
    log.info('Get chats sends chats to user')
    return render(request, 'chats.html', {'chats': chats})


def profile(request, profile_id: int):
    log.info('Profile show')
    if request.user.is_anonymous:
        log.info('Profile user is anonymous')
        return redirect(logon)
    try:
        user = User.objects.get(id=profile_id)
        user.profile.photo = str(user.profile.photo).replace('polls', '')
        log.info('Profile send profile to user')
        return render(request, 'profile.html', {'profile': user})
    except Exception as e:
        log.info('Profile user does not exist')
        return redirect(logon)


def search(request):
    log.info('Search show')
    if request.user.is_anonymous:
        log.info('Search user is anonymous')
        return redirect(logon)
    if request.method == 'POST':
        log.info('Search request is post')
        form = SearchForm(request.POST)
        if form.is_valid():
            log.info('Search form is valid')
            try:
                all_users = User.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
                users = all_users.filter(fullname__icontains=form.data['search'])
                log.info('Search send result search')
                return render(request, 'search_result.html', {'profiles': users})
            except Exception as e:
                log.info('Search is empty')
                return HttpResponse("Пользователь не найден")
    log.info('Search is empty')
    return HttpResponse("Пользователь не найден")


def change_profile(request):
    log.info('Change profile show')
    if request.user.is_anonymous:
        log.info('Change profile user is anonymous')
        return redirect(logon)
    if request.method == 'POST':
        log.info('Change profile request is post')
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            log.info('Change profile form is valid')
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
            log.info('Change profile change profile success')
            return redirect(main)
        else:
            log.info('Change profile change profile error')
            return redirect(main)
    else:
        form = ProfileForm()
        log.info('Change profile request is get')
        return render(request, 'change_profile.html', {'form': form})
