from django.urls import path
from . import views

urlpatterns = [
#   Bug 
   
    path('delete_bug/<int:bug_id>/', views.delete_bug, name='delete_bug'),
    path('edit_bug/<int:bug_id>/', views.edit_bug, name='edit_bug'),


    path('bug_list/', views.bug_list, name='bug_list'),
    path('bug_detail/<int:bug_id>/', views.bug_detail, name='bug_detail'),

#  QA
    path('create_bug/<int:project_id>/', views.create_bug, name='create_bug'),

# Developer
    path('mark_resolved/<int:bug_id>/', views.mark_resolved, name='mark_resolved'),
    path('assign_bug/<int:bug_id>/', views.assign_bug, name='assign_bug'),
]
    
    
