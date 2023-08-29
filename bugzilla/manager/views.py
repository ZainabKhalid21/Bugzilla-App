from django.shortcuts import render, redirect , get_object_or_404
from .forms import ProjectForm , AddDeveloperForm, AddQAForm , RemoveQAForm
from .models import Project
from user.models import User

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


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'edit_project.html', {'form': form, 'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return render(request, 'delete_project.html', {'project': project})


def add_developer(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = AddDeveloperForm(request.POST)
        if form.is_valid():
            developer = form.cleaned_data['developer']
            project.developer_id.add(developer)
            return redirect('project_detail', project_id=project_id)
    else:
        form = AddDeveloperForm()
    
    return render(request, 'add_developer.html', {'form': form, 'project': project})

def remove_developer(request, project_id, developer_id):
    project = get_object_or_404(Project, id=project_id)
    developer = get_object_or_404(User, id=developer_id)
    
    if request.method == 'POST':
        project.developer_id.remove(developer)
        return redirect('project_detail', project_id=project_id)
    
    return render(request, 'remove_developer.html', {'project': project, 'developer': developer})

def add_qa(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = AddQAForm(request.POST)
        if form.is_valid():
            qa = form.cleaned_data['qa']
            project.qa_id.add(qa)
            return redirect('project_detail', project_id=project_id)
    else:
        form = AddQAForm()
    
    return render(request, 'add_qa.html', {'form': form, 'project': project})

def remove_qa(request, project_id, qa_id):
    project = get_object_or_404(Project, id=project_id)
    qa = get_object_or_404(User, id=qa_id)
    
    if request.method == 'POST':
        project.qa_id.remove(qa)
        return redirect('project_detail', project_id=project_id)
    
    return render(request, 'remove_qa.html', {'project': project, 'qa': qa})