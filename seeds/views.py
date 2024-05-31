from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


from .helpers import seeds
from members import models
from todos import models as todo_models

# Create your views here.

@login_required(login_url="sevo-auth-login")
def seed_members(request):
    if request.user.is_superuser:
        try:
            member = models.Member.objects.get(firstname="Sebastian", lastname="Vogt")
            return HttpResponse("MEMBERS: WAS SEEDED IN PAST")
        except:
            seeds.do_seeds_members()
            return HttpResponse("MEMBERS: SEEDED")
    raise Http404()


@login_required(login_url="sevo-auth-login")
def delete_members_entries(request):
    if request.user.is_superuser:
        seeds.members_delete_all_entries()
        return HttpResponse("MEMBERS ENTRIES DELETED")
    raise Http404()




@login_required(login_url="sevo-auth-login")
def seed_todos(request):
    if request.user.is_superuser:
        try:
            category = todo_models.Category.objects.get(title="Allgemein")
            return HttpResponse("TODOS: WAS SEEDED IN PAST")
        except:
            seeds.do_seeds_todos(request)
            return HttpResponse("TODOS: SEEDED")
    raise Http404()




@login_required(login_url="sevo-auth-login")
def delete_todos_entries(request):
    if request.user.is_superuser:
        seeds.todos_delete_all_entries()
        return HttpResponse("TODOS ENTRIES DELETED")
    raise Http404()