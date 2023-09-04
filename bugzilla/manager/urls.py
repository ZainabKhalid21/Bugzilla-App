from django.urls import path
from . import views


urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),
    path('project_list/', views.project_list, name='project_list'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),


    path('add_developer/<int:project_id>/', views.add_developer, name='add_developer'),
    path('remove_developer/<int:project_id>/<int:developer_id>/', views.remove_developer, name='remove_developer'),
    path('add_qa/<int:project_id>/', views.add_qa, name='add_qa'),
    path('remove_qa/<int:project_id>/<int:qa_id>/', views.remove_qa, name='remove_qa'),
]

