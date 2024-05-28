from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from members import models
from members import forms


# index
@login_required(login_url="sevo-auth-login")
def index(request):
    modules = models.Module.objects.all()

    return render(request, "members/module/index.html", {
        "title": _("All modules"),
        "modules": modules
    })



# create
@login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New module was created!"))
            url = reverse("members-module-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, module was not created!"))

    else:
        form = forms.ModuleForm()

    return render(request, "members/module/create_update.html",  {
        "title": _("Create new module"),
        "form": form,
        "submit_label": _("Create")
    })



# update
@login_required(login_url="sevo-auth-login")
def update(request, id):
    module = get_object_or_404(models.Module, id=id)
    if request.method == "POST":
        form = forms.ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Module was updated!"))
            url = reverse("members-module-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, module was not updated!"))

    else:
        form = forms.ModuleForm(instance=module)

    return render(request, "members/module/create_update.html",  {
        "title": _("Update module"),
        "form": form,
        "submit_label": _("Update")
    })



# delete
login_required(login_url="sevo-auth-login")
def delete(request, id):
    module = get_object_or_404(models.Module, id=id)

    if request.method == "POST":
        module.delete()
        messages.add_message(request, messages.SUCCESS, _("Module was deleted!"))
        url = reverse("members-module-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, module was not deleted!"))
    return render(request, "members/module/delete.html", {
        "title": _("Delete module"),
        "module": module
    })

