"""proc_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from accounts import views as acc_views
from system import views

urlpatterns = [
       
    path('', views.ProductListView.as_view(), name='home'),
    path('Jobs/<int:pk>/', views.Jobs_view, name='product_jobs'),
    path('Jobs/<int:pk>/post/', views.new_job_view, name='new_job'),
    path('Jobs/<int:pk>/post/<int:post_pk>/', views.Apply_job_view, name='apply_job'),
    path('Jobs/<int:pk>/post/<int:post_pk>/decision/', views.Decision_view, name='decision'),
    path('Jobs/Client/<int:pk>/', views.chat_view, name='chat'),

        #accounts app urls using in-built class-based views
    path('signup/', acc_views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('settings/account/', acc_views.update_profile, name='my_account'),
        
        #Forgot password using in-built class-based views 
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
        name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
        name='password_reset_complete'),

        #Change password using in-built class-based view
    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
        name='password_change_done'),

    path('admin/', admin.site.urls),
] 

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

