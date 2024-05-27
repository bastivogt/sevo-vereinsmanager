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
    licenses = models.License.objects.all()

    return render(request, "members/license/index.html", {
        "title": _("All licenses"),
        "licenses": licenses
    })



# create
login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New license was created!"))
            url = reverse("members-license-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, license was not created!"))

    else:
        form = forms.LicenseForm()

    return render(request, "members/license/create_update.html",  {
        "title": _("Create new license"),
        "form": form,
        "submit_label": _("Create")
    })



# update
login_required(login_url="sevo-auth-login")
def update(request, id):
    license = get_object_or_404(models.License, id=id)
    if request.method == "POST":
        form = forms.LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("License was updated!"))
            url = reverse("members-license-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, license was not updated!"))

    else:
        form = forms.LicenseForm(instance=license)

    return render(request, "members/license/create_update.html",  {
        "title": _("Create new license"),
        "form": form,
        "submit_label": _("Update")
    })



# delete
login_required(login_url="sevo-auth-login")
def delete(request, id):
    license = get_object_or_404(models.License, id=id)

    if request.method == "POST":
        license.delete()
        messages.add_message(request, messages.SUCCESS, _("License was deleted!"))
        url = reverse("members-license-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, license was not deleted!"))

    return render(request, "members/license/delete.html", {
        "title": _("Delete license"),
        "license": license
    })

