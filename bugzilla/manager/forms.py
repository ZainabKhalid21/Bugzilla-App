from django import forms
from .models import Project
from user.models import User  # Replace this with the actual import path for your User model

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        manager_users = User.objects.filter(user_type='m')
        developer_users = User.objects.filter(user_type='d')
        qa_users = User.objects.filter(user_type='q')
        
        self.fields['manager_id'].queryset = manager_users
        self.fields['developer_id'].queryset = developer_users
        self.fields['qa_id'].queryset = qa_users
        
  
    class Meta:
        model = Project
        fields = ['project_name', 'project_id', 'manager_id', 'developer_id', 'qa_id']

class AddQAForm(forms.Form):
    qa = forms.ModelChoiceField(queryset=User.objects.filter(user_type='q'), label='Select QA')

class AddDeveloperForm(forms.Form):
    developer = forms.ModelChoiceField(queryset=User.objects.filter(user_type='d'), label='Select Developer')

class RemoveQAForm(forms.Form):
    pass