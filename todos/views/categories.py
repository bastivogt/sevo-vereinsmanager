from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from todos import models
from todos import forms


# index
@login_required(login_url="sevo-auth-login")
def index(request):
    categories = models.Category.objects.all()
    print(categories)

    return render(request, "todos/category/index.html", {
        "title": _("All Categories"),
        "categories": categories
    })

# create
@login_required(login_url="sevo-auth-login")
def create(request):
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Category was created!"))
            url = reverse("todos-category-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, category was not created!"))

    else:
        form = forms.CategoryForm()
    return render(request, "todos/category/create_update.html", {
        "title": _("Create category"),
        "form": form,
        "submit_label": _("Create")
    })


# update
@login_required(login_url="sevo-auth-login")
def update(request, id):
    category = get_object_or_404(models.Category, id=id)
    if request.method == "POST":
        form = forms.CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Category was updated!"))
            url = reverse("todos-category-index")
            return HttpResponseRedirect(url)
        else:
            messages.add_message(request, messages.ERROR, _("Failed, category was not updated!"))

    else:
        form = forms.CategoryForm(instance=category)
    return render(request, "todos/category/create_update.html", {
        "title": _("Update category") + f" #{category.id}",
        "form": form,
        "submit_label": _("Update")
    })



# delete
@login_required(login_url="sevo-auth-login")
def delete(request, id):
    category = get_object_or_404(models.Category, id=id)

    if request.method == "POST":
        category.delete()
        messages.add_message(request, messages.SUCCESS, _("Category was deleted!"))
        url = reverse("todos-category-index")
        return HttpResponseRedirect(url)
    else:
        messages.add_message(request, messages.SUCCESS, _("Failed, category was not deleted!"))

    return render(request, "todos/category/delete.html", {
        "title": _("Delete category") + f" #{category.id}",
        "category": category
    })
