from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('logon/', views.logon, name='logon'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
    path('main/<int:profile_id>', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('search', views.search, name='search'),
    path('messages/<int:sender_id>', views.get_messages, name='messages'),
    path('chats/', views.get_chats, name='chats'),
    path('chat/<int:sender_id>', views.get_chat, name='chat'),
    path('change_profile',views.change_profile,name="change_profile"),
    path('send_message',views.send_message, name="send_message"),
    # path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
