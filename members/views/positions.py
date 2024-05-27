from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from members import models
from members import forms


# index
login_required(login_url="sevo-auth-login")
def index(request):
    positions = models.Position.objects.all()

    return render(request, "members/position/index.html", {
        "title": _("All positions"),
        "genders": positions
    })



# create
login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.GenderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New position was created!"))
            url = reverse("members-position-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, position was not created!"))

    else:
        form = forms.GenderForm()

    return render(request, "members/position/create_update.html",  {
        "title": _("Create new position"),
        "form": form,
        "submit_label": _("Create")
    })



# update
login_required(login_url="sevo-auth-login")
def update(request, id):
    position = get_object_or_404(models.Position, id=id)
    if request.method == "POST":
        form = forms.GenderForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New position was created!"))
            url = reverse("members-position-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, position was not created!"))

    else:
        form = forms.GenderForm(instance=position)

    return render(request, "members/gender/create_update.html",  {
        "title": _("Create new position"),
        "form": form,
        "submit_label": _("Update")
    })



# delete
login_required(login_url="sevo-auth-login")
def delete(request, id):
    position = get_object_or_404(models.Position, id=id)

    if request.method == "POST":
        position.delete()
        messages.add_message(request, messages.SUCCESS, _("Position was deleted!"))
        url = reverse("members-gender-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, position was not deleted!"))
    return render(request, "members/position/delete.html", {
        "title": _("Delete gender"),
        "gender": position
    })

