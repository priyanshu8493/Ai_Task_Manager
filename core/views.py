from django.shortcuts import render
from .models import tasks
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.http import HttpResponseBadRequest
from django.utils import timezone


def home(request):

    all_tasks = tasks.objects.all()
    context = {'all_tasks' : all_tasks}

    return render(request, 'home.html', context)



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
    

def delete_task(request, task_id):
    if request.method == 'POST':
        task = tasks.objects.get(pk = task_id)
        task.delete()
    return redirect ('home')
    
