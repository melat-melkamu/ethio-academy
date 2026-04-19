from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('logout-confirm/', views.logout_confirm, name='logout_confirm'),
    path('logout-execute/', views.user_logout, name='logout_execute'),
    
    path('after-login/', views.login_success_redirect, name='after_login'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard')
]