from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

@login_required
def home(request):

    all_tasks = tasks.objects.all()
    context = {'all_tasks' : all_tasks}

    return render(request, 'home.html', context)


@login_required
def create_task(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline_str = request.POST.get('deadline')
        deadline = parse_date(deadline_str)

        if deadline < timezone.now().date():
            return HttpResponseBadRequest("Deadline cannot be in the past.")

        # new instance of task

        new_task = tasks.objects.create(
            title = title,
            description = description,
            status = status,
            deadline = deadline
        )
        # returning to the homepage with all tasks view
        return redirect ('home')

    return render (request,'create.html')
    


@login_required
def update_task(request, task_id):

    req_task = tasks.objects.get( pk = task_id )

    if request.method == 'POST':
        req_task.title = request.POST.get('title')
        req_task.description = request.POST.get('description')
        req_task.status = request.POST.get('status')
        req_task.deadline = request.POST.get('deadline')

        req_task.save()

        return redirect ('home')
    

    return render(request, 'update.html', {'task':req_task})
    
@login_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = tasks.objects.get(pk = task_id)
        task.delete()
    return redirect ('home')
    


## adding user login and registration


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if already exists or not
        if not User.objects.filter( username = username ).exists():
            messages.error(request, "Invalid Username")
            return redirect('login_view')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('login_view')
        
        else:
            login(request,user)
            return redirect('home')
        
    return render(request,'login.html')
        

