from django import forms
from .models import Project
from user.models import User 

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        developer_users = User.objects.filter(user_type='d')
        qa_users = User.objects.filter(user_type='q')
        

        self.fields['developer_id'].queryset = developer_users
        self.fields['qa_id'].queryset = qa_users
        
  
    class Meta:
        model = Project
        fields = ['project_name','manager_id', 'developer_id', 'qa_id']

class AddQAForm(forms.Form):
    qa = forms.ModelChoiceField(queryset=User.objects.filter(user_type='q'), label='Select QA')

class AddDeveloperForm(forms.Form):
    developer = forms.ModelChoiceField(queryset=User.objects.filter(user_type='d'), label='Select Developer')

class RemoveQAForm(forms.Form):
    pass