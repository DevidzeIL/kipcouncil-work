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
    path('more/<str:pk_test>/', views.more, name="more"),

    path('calendar/', views.calendar_view, name="calendar"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('user/', views.mainUser, name="main_user"),
    path('account/', views.accountSettings, name="account_settings"),

    path('create_award/<str:pk_test>/', views.createAward, name="create_award"),
    path('edit_award/<str:pk_test>/', views.editAward, name="edit_award"),
    path('delete_award/<str:pk_test>/', views.deleteAward, name="delete_award"),



    path('user_table/<str:pk_test>/', views.userTable, name="user_table"),
    path('admin_table/', views.adminTable, name="admin_table"),
    path('admin_lookuser/<str:pk_test>/', views.adminLookuser, name="admin_lookuser"),


    path('admin_tabledb/<str:pk_test>/', views.adminTableDB, name="admin_tabledb"),


    path('admin_createdb/<str:pk_test>/', views.adminCreateDB, name="admin_createdb"),
    path('admin_editdb/<str:pk_test1>/<str:pk_test2>/', views.adminEditDB, name="admin_editdb"),
    path('admin_deletedb/<str:pk_test1>/<str:pk_test2>/', views.adminDeleteDB, name="admin_deletedb"),

    path('admin_massivecreatedb/<str:pk_test1>/<str:pk_test2>/', views.adminMassiveCreateDB, name="admin_massivecreatedb"),



    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='accounts/auth/password/password_reset.html'),
     name = 'reset_password'),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/auth/password/password_reset_sent.html'),
    name = 'password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/auth/password/password_reset_form.html'),
    name = 'password_reset_confirm'),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/auth/password/password_reset_done.html'),
    name = 'password_reset_complete'),

    path('view_404/', views.view_404, name="view_404"),
    path('secret/', views.secret, name="secret"),
]




from django.shortcuts import render
from django.template import RequestContext


# def handler404(request, *args, **argv):
#     response = render('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# handler404 = handler404
