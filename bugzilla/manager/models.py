from django.db import models
from user.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    manager_id=models.ForeignKey(User, on_delete=models.CASCADE , related_name='bug_manager')
    developer_id=models.ManyToManyField(User ,  related_name='bug_developer')
    qa_id=models.ManyToManyField(User , related_name='bug_qa')