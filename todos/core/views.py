from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Todo

# Create your views here.

def index(request):
    todos=Todo.objects.all()
    return render(request,'core/index.html', {"todos":todos})

def create_todo(request):
    params = request.POST
    todo=Todo(
        content=params.get("content")
    )
    todo.save()
    return redirect("/")

def update_todo(request:HttpRequest, id):
    todo=Todo.objects.get(id=id)
    todo.is_completed=request.POST.get("is_completed")=="true"
    todo.save()
    return JsonResponse({"success":True})
