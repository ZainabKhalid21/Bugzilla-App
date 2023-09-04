from django.db import models
from django.db import models
from user.models import User
from manager.models import Project
from cloudinary.models import CloudinaryField
from .enums import BugStatus, BugType
from django.core.exceptions import ValidationError
from django.utils import timezone
def validate_cloudinary_image_extension(value):
    allowed_extensions = ['png', 'gif']
    file_extension = value.format.split('.')[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValidationError('Only PNG and GIF images are allowed.')

class Bug(models.Model):
    bug_title = models.CharField(max_length=100)
    bug_deadline = models.DateTimeField() 
    bug_screenshot = CloudinaryField('image' , 
                            blank=True,
                            validators=[validate_cloudinary_image_extension])
    
    qa_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_creator')
    developer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_solver')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bugs')

    bug_type = models.CharField(max_length=10, choices=[(tag.value, tag.name) for tag in BugType])
    bug_status = models.CharField(max_length=10, choices=[(status.value, status.name) for status in BugStatus])

    def clean(self):
        super().clean()
        current_time = timezone.now()
        if self.bug_deadline <= current_time:
            raise ValidationError("Bug deadline must be in the future.")
    
        
        # existing_bugs = Bug.objects.filter(bug_title=self.bug_title)
        # if self.pk:
        #     existing_bugs = existing_bugs.exclude(pk=self.pk)
        # if existing_bugs.exists():
        #     raise ValidationError("Bug with this title already exists in the project.")

        existing_bugs = Bug.objects.filter(bug_title=self.bug_title, project_id=self.project_id_id)
        if self.pk:
            existing_bugs = existing_bugs.exclude(pk=self.pk)
        if existing_bugs.exists():
            raise ValidationError("Bug with this title already exists in the project.")

        
    class Meta:
        unique_together = ('bug_title', 'project_id')
    