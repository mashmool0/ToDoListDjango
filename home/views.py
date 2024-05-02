from django.shortcuts import render, redirect
from .models import Tasks


def home(request):
    if request.method == 'POST':
        if 'task' in request.POST:
            taskname = request.POST['task']
            Tasks.objects.create(Taskname=taskname)
            return redirect('/')
        if 'delete_task' in request.POST:
            if Tasks.objects.count() > 0 :
                Tasks.objects.get(id=request.POST['delete_task']).delete()


    tasks_list = Tasks.objects.all()[::-1]
    return render(request, 'home/home.html', context={"task_list": tasks_list})
