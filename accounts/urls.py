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
    path('admin_users/', views.adminUsers, name="admin_users"),



    path('admin_adduser/', views.adminAddUser, name="admin_adduser"),
    path('admin_addtag/', views.adminAddTag, name="admin_addtag"),
    path('admin_addevent/', views.adminAddEvent, name="admin_addevent"),
    path('admin_addmember/', views.adminAddMember, name="admin_addmember"),
    path('admin_addnew/', views.adminAddNew, name="admin_addnew"),


    path('admin_workdb/<str:pk_test>/', views.adminWorkDB, name="admin_workdb"),
    path('admin_editdb/<str:pk_test>/', views.adminEditDB, name="admin_editdb"),
    

    # path('admin_edituser/', views.adminEditUser, name="admin_edituser"),
    # path('admin_editevent/', views.adminEditEvent, name="admin_editevent"),
    # path('admin_editmember/', views.adminEditMember, name="admin_editmember"),
    # path('admin_editnew/', views.adminEditNew, name="admin_editnew"),

    # path('admin_deleteuser/', views.adminDeleteUser, name="admin_deleteuser"),
    # path('admin_deleteevent/', views.adminDeleteEvent, name="admin_deleteevent"),
    # path('admin_deletemember/', views.adminDeleteMember, name="admin_deletemember"),
    # path('admin_deletenew/', views.adminDeleteNew, name="admin_deletenew"),



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