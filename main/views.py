from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Todo
# Create your views here.
def home(request):
    # todo_items = Todo.objects.all().order_by('added_date')
    # return render(request, 'outside/index.html', {'todo_items': todo_items})
    return render(request, 'outside/index.html', {'todo_items': Todo.objects.all().order_by('-added_date')[:5]})

@csrf_exempt
def add_todo(request):  # form => only logic and HttpResponseRedirect
    print(request.POST)
    # return HttpResponse('hi %s' % request.POST['todo'])
    # return HttpResponse('{}'.format('Add to do:\t%s' % request.POST['todo']))
    # return HttpResponse('Add to do:\t{}'.format(request.POST['todo']))

    if request.POST['todo'] == '':
        return render(request, 'outside/index.html', {'error_message': "todo field can't be blank. Please fill out."})

    # added_date = timezone.now()
    # todo = request.POST['todo']
    # print(added_date, todo)

    # Todo.objects.create(added_date=added_date, text=todo)
    create_obj = Todo.objects.create(added_date=timezone.now(), text=request.POST['todo'])

    print(create_obj, '\n', create_obj.id, '\n', Todo.objects.all().count())

    # return render(request, 'outside/index.html', {'todo_items': Todo.objects.all()})
    return HttpResponseRedirect('/')

    # return HttpResponseRedirect('')
    #  #call again url => localhost:8000/add_todo and
    # get error MultiValueDictKeyError at /add_todo/    'todo'


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
