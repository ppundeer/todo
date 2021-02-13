from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoItem
from .forms import *

def todoView(request):
    todo_items = todoItem.objects.all()
    form = todoForm()   #initial={'content': "Write task..."})

    if request.method =='POST':
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')

    return render(request, 'todo.html',
                  {'all_items': todo_items, 'form': form})

def updateTodo(request, pk):
    todos = todoItem.objects.get(id=pk)
    form = todoForm(instance=todos)

    if request.method == 'POST':
        form = todoForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
        return redirect('/todo/')

    return render(request, 'update.html', {'form': form})

def deleteTodo(request, todo_id):
    item = todoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo/')

    return render(request, 'delete.html', {'item': item})