from django import forms
from django.utils.translation import gettext as _

from . import models


# GenderForm
class GenderForm(forms.ModelForm):
    
    class Meta:
        model = models.Gender
        fields = "__all__"
        labels = {
            "title": _("Title")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }


# GenderForm
class PositionForm(forms.ModelForm):
    
    class Meta:
        model = models.Gender
        fields = "__all__"
        labels = {
            "title": _("Title")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }
        