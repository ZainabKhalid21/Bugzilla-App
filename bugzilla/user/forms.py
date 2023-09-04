from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class Registration(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=get_user_model().User_types)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'user_email', 'user_type']
