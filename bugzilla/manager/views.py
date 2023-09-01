from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm , AddDeveloperForm, AddQAForm 
from .models import Project
from .decorators import get_project
from user.models import User


#******************************************PROJECT****************************************#

def custom_404(request, exception):
    return render(request, 'error404.html', status=500)

@login_required
def project_list(request):
    if request.user.user_type == 'd':
        projects = Project.objects.filter(developer_id=request.user)
    else:
        projects = Project.objects.all()
    
    return render(request, 'project_list.html', {'projects': projects})

@login_required
@get_project
def project_detail(request, project):
    return render(request, 'project_detail.html', {'project': project})


#******************************************MANAGER CRUD****************************************#
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.manager = request.user 
            project.save()
            form.save_m2m()  
            return redirect('project_list') 
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
@get_project
def edit_project(request, project):
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'edit_project.html', {'form': form, 'project': project})

@login_required
@get_project
def delete_project(request, project):
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return render(request, 'delete_project.html', {'project': project})

#******************************************MANAGER ADD AND REMOVE DEVELOPER****************************************#
@login_required
@get_project
def add_developer(request, project):
    if request.method == 'POST':
        form = AddDeveloperForm(request.POST)
        if form.is_valid():
            developer = form.cleaned_data['developer']
            project.developer_id.add(developer)
            return redirect('project_detail', project_id=project.id)
    else:
        form = AddDeveloperForm()
    
    return render(request, 'add_developer.html', {'form': form, 'project': project})

@login_required
@get_project
def remove_developer(request, project, developer_id):
    developer = get_object_or_404(User, id=developer_id)
    
    if request.method == 'POST':
        project.developer_id.remove(developer)
        return redirect('project_detail', project_id=project.id)
    
    return render(request, 'remove_developer.html', {'project': project, 'developer': developer})


#******************************************MANAGER ADD AND REMOVE QA****************************************#
@login_required
@get_project
def add_qa(request, project):
    
    if request.method == 'POST':
        form = AddQAForm(request.POST)
        if form.is_valid():
            qa = form.cleaned_data['qa']
            project.qa_id.add(qa)
            return redirect('project_detail', project_id=project.id)
    else:
        form = AddQAForm()
    
    return render(request, 'add_qa.html', {'form': form, 'project': project})

@login_required
@get_project
def remove_qa(request, project, qa_id):
    qa = get_object_or_404(User, id=qa_id)
    
    if request.method == 'POST':
        project.qa_id.remove(qa)
        return redirect('project_detail', project_id=project.id)
    
    return render(request, 'remove_qa.html', {'project': project, 'qa': qa})


    #*********************************************************************************************#