from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import TodoForm
from .models import Todo


class TodoListView(View):

    def get(self, request):
        form = TodoForm()
        item_list = Todo.objects.filter(created_by=request.user.id)
        context = {
            'todos': item_list,
            'form': form
        }
        return render(request, 'todo/index.html', context)


class AddTodoView(View):
    def post(self, request):
        form = TodoForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by_id = request.user.id
                obj.save()
                messages.success(request, "Successfully created")
        return redirect('todo:todo-list')


class UpdateTodoView(View):
    def post(self, request):
        if request.method == 'POST':
            pk = request.POST.get('pk')
            data = Todo.objects.get(pk=pk)
            data.title = request.POST.get('title')
            data.date = request.POST.get('date')
            data.created_by_id = request.user.id
            data.save()
            messages.success(request, "Successfully updated")
        return redirect('todo:todo-list')


class EditTodoView(View):
    def get(self, request, pk):
        data = Todo.objects.get(pk=pk)
        context = {
            'data': data
        }
        return render(request, 'todo/edit.html', context)


class DeleteTodoView(View):
    def get(self, request, pk):
        data = Todo.objects.get(pk=pk)
        data.delete()
        messages.success(request, "Data deleted")
        return redirect('todo:todo-list')

