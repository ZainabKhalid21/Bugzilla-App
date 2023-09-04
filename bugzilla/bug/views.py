from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bug , BugStatus 
from .forms import BugForm
from manager.models import Project
from .decorators import user_role_required

#******************************************Bug ROLES****************************************#

def custom_404(request, exception):
    return render(request, 'error404.html', status=500)

@login_required
def bug_detail(request, bug_id):
    bug = get_object_or_404(Bug, id = bug_id)
    return render(request, 'bug_detail.html', {'bug': bug})

@login_required
def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_list.html', {'bugs': bugs})

#******************************************QA ROLES****************************************#    

@login_required
@user_role_required(allowed_roles=['q'])
def create_bug(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.qa_id = request.user
            bug.project_id = project
            bug.developer_id = request.user
            bug.save()
            
            return redirect('bug_detail', bug.id)
    else:
        initial_data = {'bug_type': 'bug'}
        form = BugForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'create_bug.html', context)


@login_required
@user_role_required(allowed_roles=['q'])
def edit_bug(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)

    if request.user.user_type == 'q':
        if request.method == 'POST':
            form = BugForm(request.POST, instance=bug)
            if form.is_valid():
                form.save()
                return redirect('bug_detail', bug_id=bug_id)
        else:
            form = BugForm(instance=bug)
        context = {'form': form, 'bug': bug}
        return render(request, 'edit_bug.html', context)
    else:
        return redirect('bug_detail', bug_id=bug_id)

@login_required
@user_role_required(allowed_roles=['q'])
def delete_bug(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    if request.user.user_type == 'q':
        if request.method == 'POST':
            bug.delete()
            return redirect('bug_list')
        context = {'bug': bug}
        return render(request, 'delete_bug.html', context)
    else:
        return redirect('bug_detail', bug_id=bug_id)

#******************************************DEVELOPER ROLES****************************************#
@login_required
@user_role_required(allowed_roles=['d'])
def assign_bug(request, bug_id):
    bug = Bug.objects.get(pk=bug_id)
    
    if request.method == 'POST':
        if request.user.user_type == 'd' and bug.bug_status == BugStatus.NEW.value:
            bug.developer_id = request.user
            bug.bug_status = BugStatus.STARTED.value 
            bug.save()
            return redirect('bug_detail', bug_id=bug_id)
    show_assign_button = False
    if request.user.user_type == 'd' and bug.bug_status == BugStatus.NEW.value:
        show_assign_button = True
        
    return render(request, 'assign_bug.html', {'bug': bug, 'show_assign_button': show_assign_button})

@login_required
@user_role_required(allowed_roles=['d'])
def mark_resolved(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id, developer_id=request.user, bug_status='started')
    if request.method == 'POST':
        if bug.bug_status == 'started':
            bug.bug_status = 'resolved'
            bug.save()
            return redirect('bug_detail', bug_id=bug_id)
        
    
    show_resolve_button = False
    if request.user.user_type == 'd' and (bug.bug_status == 'started' or bug.bug_status == 'new'):
        show_resolve_button = True
        
    return render(request, 'mark_resolved.html', {'bug': bug, 'show_resolve_button': show_resolve_button})
