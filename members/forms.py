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


# PositionForm
class PositionForm(forms.ModelForm):
    
    class Meta:
        model = models.Position
        fields = "__all__"
        labels = {
            "title": _("Title")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }




# ModuleForm
class ModuleForm(forms.ModelForm):
    
    class Meta:
        model = models.Module
        fields = "__all__"
        labels = {
            "title": _("Title")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }
