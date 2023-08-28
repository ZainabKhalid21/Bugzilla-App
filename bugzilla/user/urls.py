from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  ForgotPassword, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView



urlpatterns = [
    path('signup/', views.signup, name = 'signup'  ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#    Forgot password
    path('forgot_password/', ForgotPassword.as_view(), name='forgot_password'),
    path('password_reset/', CustomPasswordResetDoneView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('homepage/', views.homepage, name='homepage'),

    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

]