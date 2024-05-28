from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from members import models
from members import forms
from members.views.helper import filter




def redirect(request):
    url = reverse("members-member-index")
    return HttpResponseRedirect(url)


@login_required(login_url="sevo-auth-login")
def index(request):
    members = models.Member.objects.all()

    positions = models.Position.objects.all()
    modules = models.Module.objects.all()
    tariffs = models.Tariff.objects.all()
    licenses = models.License.objects.all()
    genders = models.Gender.objects.all()

    members = filter.filter(request, members)

    return render(request, "members/member/index.html", {
        "title": _("All members"),
        "members": members,
        "positions": positions,
        "modules": modules,
        "tariffs": tariffs,
        "licenses": licenses,
        "genders": genders
    })



# create
@login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New member was created!"))
            url = reverse("members-member-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, member was not created!"))

    else:
        form = forms.MemberForm()

    return render(request, "members/member/create_update.html",  {
        "title": _("Create new Member"),
        "form": form,
        "submit_label": _("Create")
    })


# update
@login_required(login_url="sevo-auth-login")
def update(request, id):
    member = get_object_or_404(models.Member, id=id)
    if request.method == "POST":
        form = forms.MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Member was updated!"))
            url = reverse("members-member-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, member was not created!"))

    else:
        form = forms.MemberForm(instance=member)

    return render(request, "members/member/create_update.html",  {
        "title": _("Update member"),
        "form": form,
        "submit_label": _("Update")
    })


# detail
@login_required(login_url="sevo-auth-login")
def detail(request, id):
    member = get_object_or_404(models.Member, id=id)
    return render(request, "members/member/detail.html", {
        "title": _("Detail member"), 
        "member": member
    })


