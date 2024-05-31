from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


from .helpers import seeds
from members import models

# Create your views here.

@login_required(login_url="sevo-auth-login")
def index(request):
    if request.user.is_superuser:
        try:
            member = models.Member.objects.get(firstname="Sebastian", lastname="Vogt")
            return HttpResponse("WAS SEEDED IN PAST")
        except:
            seeds.do_seeds()
            return HttpResponse("SEEDED")
    raise Http404()


@login_required(login_url="sevo-auth-login")
def delete_members_entries(request):
    if request.user.is_superuser:
        seeds.members_delete_all_entries()
        return HttpResponse("MEMBERS ENTRIES DELETED")
    raise Http404()