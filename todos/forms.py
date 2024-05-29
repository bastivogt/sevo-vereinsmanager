from django import forms
from django.utils.translation import gettext as _
from tinymce.widgets import TinyMCE

from . import models

# CategoryForm
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = models.Category
        fields = "__all__"
        labels = {
            "title": _("Title"),
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
        }


# TodoForm
class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = "__all__"
        exclude = [
            "user"
        ]

        labels = {
            "title": _("Title"),
            "content": _("Content"),
            "categories": _("Categories"),
            "done": _("Done")
        }

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": TinyMCE(attrs={"cols": 80, "rows": 30, "class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-select multiple"}),
            "done": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }