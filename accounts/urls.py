from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('direction/<str:tags>/', views.direction, name="direction"),
    path('about/', views.about, name="about"),
    path('docs_college/', views.docs_college, name="docs_college"),
    path('docs_council/', views.docs_council, name="docs_council"),
    path('news_about/<str:pk_test>/', views.news_about, name="news_about"),
    path('news/', views.news, name="news"),
    
    path('search/', views.search, name="search"),
    path('calendar/', views.calendar_view, name="calendar"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),


    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name='accounts/auth/password_reset.html'),
     name = 'reset_password'),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/auth/password_reset_sent.html'),
    name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/auth/password_reset_form.html'),
    name = 'password_reset_confirm'),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/auth/password_reset_done.html'),
    name = 'password_reset_complete'),
]