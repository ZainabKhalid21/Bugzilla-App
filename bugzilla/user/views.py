from django.contrib.auth import get_user_model
import logging
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import Registration , UserForm
from .models import User
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LoginView,  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

User = get_user_model()

#**************************************SIGNUP********************************************************#
def signup(request):
    
   
    if request.method == 'POST':
        form = Registration(request.POST)
        print(form.errors) 
        if form.is_valid():
            user = form.save()
            return redirect('login') 
    else:
        form = Registration()
    return render(request, 'signup.html', {'form': form})

#**************************************LOGIN********************************************************#
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    
    
#***********************************FORGOT PASSWORD*********************************************************#

class ForgotPassword(PasswordResetView):
    template_name = 'forgot_password.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset')

    def form_valid(self, form):
        email = form.cleaned_data['email'] 
        user = User.objects.get(email=email)  

    
        token = default_token_generator.make_token(user)

    
        reset_url = self.request.build_absolute_uri(reverse_lazy('password_reset_confirm', 
        kwargs={
            'uidb64': self.request.user.pk,
            'token': token,
        }))

        send_mail(
            subject='Password Reset',
            message=f'Click the following link to reset your password: {reset_url}',
            from_email= settings.EMAIL_HOST_USER ,
            recipient_list=[user.email],
        )

        return super().form_valid(form)
    logging.info(f"Password reset email sent ")
    

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


#************************************HOMEPAGE*************************************************************#

@login_required
def homepage(request):
    return render(request, 'homepage.html')



#**************************************CRUD OPERATIONS***********************************************#

@login_required

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Registration(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user_list')
        else:
            form = Registration()
        return render(request, 'user_create.html', {'form': form})
    else:
        return redirect('user_list') 

@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user.is_superuser and not user.is_superuser:
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('user_list')
        else:
            form = UserForm(instance=user)
        return render(request, 'user_edit.html', {'form': form, 'user': user})
    else:
        return redirect('user_list')  

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user.is_superuser and not user.is_superuser and user != request.user:
        if request.method == 'POST':
            user.delete()
            return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})

#************************************************************************************************************#