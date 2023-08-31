from django.db import models
from django.db import models
from user.models import User
from manager.models import Project
from cloudinary.models import CloudinaryField
from .enums import BugStatus, BugType


class Bug(models.Model):
    bug_title = models.CharField(max_length=100)
    bug_deadline = models.DateTimeField() 
    bug_screenshot = CloudinaryField('image' , blank= True)
    
    qa_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_creator')
    developer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_solver')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')

    bug_type = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in BugType])
    bug_status = models.CharField(max_length=10, choices=[(status.value, status.name) for status in BugStatus])


    class Meta:
        unique_together = ('bug_title', 'project_id')

    