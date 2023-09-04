from django import forms
from .models import Bug
from cloudinary.forms import CloudinaryFileField


class BugForm(forms.ModelForm):
    bug_screenshot = CloudinaryFileField(required=False)

    class Meta:
        model = Bug
        fields = ['bug_title', 'bug_deadline', 'bug_screenshot' , 'bug_type' , 'bug_status']
        

    