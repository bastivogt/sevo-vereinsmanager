from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()



from todos import models
from todos import forms
from todos.views.helper import filter
from todos import exceptions
from todos.views.helper import todo_helper

@login_required(login_url="sevo-auth-login")
def index(request):
    todos = models.Todo.objects.all()
    categories = models.Category.objects.all()

    todos = filter.filter(request, todos)

    return render(request, "todos/todo/index.html", {
        "title": "All todos",
        "todos": todos,
        "categories": categories
    })


# create
@login_required(login_url="sevo-auth-login")
def create(request):
    user = request.user
    todo = models.Todo(user=user)
    if request.method == "POST":
        form = forms.TodoFormCreate(request.POST, instance=todo)
        if form.is_valid():
            form.save(request.user)
            messages.add_message(request, messages.SUCCESS, _("Todo was created!"))
            url = reverse("todos-todo-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, todo was not created!"))

    else:
        form = forms.TodoFormCreate(instance=todo)
    return render(request, "todos/todo/create_update.html", {
        "title": _("Create todo"),
        "form": form,
        "submit_label": _("Create")
    })



# update
@login_required(login_url="sevo-auth-login")
def update(request, id):
    todo = get_object_or_404(models.Todo, id=id)
    if request.method == "POST":
        form = forms.TodoForm(request.POST, instance=todo)
        if form.is_valid():
            try:
                form.save(request.user)
            except exceptions.InvalidUserExcpetion as e:
                pass
                # messages.add_message(request, messages.ERROR, e)

 
            messages.add_message(request, messages.SUCCESS, _("Todo was updated!"))
            url = reverse("todos-todo-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, todo was not updated!"))

    else:
        form = forms.TodoForm(instance=todo)
    return render(request, "todos/todo/create_update.html", {
        "title": _("Update todo") + f" #{todo.id}",
        "form": form,
        "submit_label": _("Update")
    })



# delete
@login_required(login_url="sevo-auth-login")
def delete(request, id):
    todo = get_object_or_404(models.Todo, id=id)

    if request.method == "POST":
        todo.delete()
        messages.add_message(request, messages.SUCCESS, _("Todo was deleted!"))
        url = reverse("todos-todo-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, todo was not deleted!"))

    return render(request, "todos/todo/delete.html", {
        "title": _("Delete todo") + f" #{todo.id}",
        "todo": todo
    })


# detail
@login_required(login_url="sevo-auth-login")
def detail(request, id):
    todo = get_object_or_404(models.Todo, id=id)
    return render(request, "todos/todo/detail.html", {
        "title": _("Todo detail") + f" #{todo.id}",
        "todo": todo
    })

# done
@login_required(login_url="sevo-auth-login")
def done(request, id):
    return todo_helper.done(request=request, id=id, path_name="todos-todo-index")



# done_from_detail
@login_required(login_url="sevo-auth-login")
def done_from_detail(request, id):
    return todo_helper.done(request=request, id=id, path_name="todos-todo-detail", path_id=id)
