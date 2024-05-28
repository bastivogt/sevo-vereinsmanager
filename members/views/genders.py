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
    genders = models.Gender.objects.all()

    return render(request, "members/gender/index.html", {
        "title": _("All genders"),
        "genders": genders
    })



# create
login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.GenderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("New gender was created!"))
            url = reverse("members-gender-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, gender was not created!"))

    else:
        form = forms.GenderForm()

    return render(request, "members/gender/create_update.html",  {
        "title": _("Create new gender"),
        "form": form,
        "submit_label": _("Create")
    })



# update
login_required(login_url="sevo-auth-login")
def update(request, id):
    gender = get_object_or_404(models.Gender, id=id)
    if request.method == "POST":
        form = forms.GenderForm(request.POST, instance=gender)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Gender was created!"))
            url = reverse("members-gender-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, gender was not created!"))

    else:
        form = forms.GenderForm(instance=gender)

    return render(request, "members/gender/create_update.html",  {
        "title": _("update gender"),
        "form": form,
        "submit_label": _("Update")
    })



# delete
login_required(login_url="sevo-auth-login")
def delete(request, id):
    gender = get_object_or_404(models.Gender, id=id)

    if request.method == "POST":
        gender.delete()
        messages.add_message(request, messages.SUCCESS, _("Gender was deleted!"))
        url = reverse("members-gender-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, gender was not deleted!"))

    return render(request, "members/gender/delete.html", {
        "title": _("Delete gender"),
        "gender": gender
    })

