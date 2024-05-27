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
    tariffs = models.Tariff.objects.all()

    return render(request, "members/tariff/index.html", {
        "title": _("All tariffs"),
        "tariffs": tariffs
    })



# create
login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.TariffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New tariff was created!"))
            url = reverse("members-tariff-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, tariff was not created!"))

    else:
        form = forms.TariffForm()

    return render(request, "members/tariff/create_update.html",  {
        "title": _("Create new tariff"),
        "form": form,
        "submit_label": _("Create")
    })



# update
login_required(login_url="sevo-auth-login")
def update(request, id):
    tariff = get_object_or_404(models.Tariff, id=id)
    if request.method == "POST":
        form = forms.TariffForm(request.POST, instance=tariff)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Tariff was upadated!"))
            url = reverse("members-tariff-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, tariff was not updated!"))

    else:
        form = forms.TariffForm(instance=tariff)

    return render(request, "members/tariff/create_update.html",  {
        "title": _("Create new tariff"),
        "form": form,
        "submit_label": _("Update")
    })



# delete
login_required(login_url="sevo-auth-login")
def delete(request, id):
    tariff = get_object_or_404(models.Tariff, id=id)

    if request.method == "POST":
        tariff.delete()
        messages.add_message(request, messages.SUCCESS, _("Tariff was deleted!"))
        url = reverse("members-tariff-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, tariff was not deleted!"))

    return render(request, "members/tariff/delete.html", {
        "title": _("Delete tariff"),
        "tariff": tariff
    })

