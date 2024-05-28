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


# LicenseForm
class LicenseForm(forms.ModelForm):
    
    class Meta:
        model = models.License
        fields = "__all__"
        labels = {
            "title": _("Title")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"})
        }



# TariffForm
class TariffForm(forms.ModelForm):
    
    class Meta:
        model = models.Tariff
        fields = "__all__"
        labels = {
            "title": _("Title"),
            "amount": _("Amount")
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"})
        }




# MemberForm
class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = "__all__"
        labels = {
            "firstname": _("Firstname"),
            "lastname": _("Lastname"),
            "birthday": _("Birthday"),
            "gender": _("Gender"),

            "street": _("Street"),
            "house_number": _("House number"),
            "postal_code": _("Postal code"),
            "city": _("City"),
            "country": _("Country"),

            "email": _("Email"),
            "phone": _("Phone"),

            "legal_representative": _("Legal reprensentative"),
            
            "bankname": _("Bank name"),
            "iban": _("IBAN"),
            "bic": _("BIC"),

            "positions": _("Positions"),
            "modules": _("Modules"),
            "licenses": _("Licenses"),
            "tariff": _("Tariff"),

            "Chronic_diseases": _("Chronic diseases"),
            "permanent_medication": _("Permanent medication"),

            "publish_fotos": _("Publish fotos"),
            "is_active": _("Is active"),

            "created_at": _("Created at"),
            "updated_at": _("Updated at")
        }

        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "birthday": forms.DateInput(format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": _("Choose a date"), "type":"date"}),
            "gender": forms.Select(attrs={"class": "form-select"}),

            "street": forms.TextInput(attrs={"class": "form-control"}),
            "house_number": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),

            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),

            "legal_representative": forms.Textarea(attrs={"class": "form-control"}),

            "bankname": forms.TextInput(attrs={"class": "form-control"}),
            "iban": forms.TextInput(attrs={"class": "form-control"}),
            "bic": forms.TextInput(attrs={"class": "form-control"}),

            "positions": forms.SelectMultiple(attrs={"class": "form-select"}),
            "modules": forms.SelectMultiple(attrs={"class": "form-select"}),
            "licenses": forms.SelectMultiple(attrs={"class": "form-select"}),
            "tariff": forms.Select(attrs={"class": "form-select"}),
            "entry_date": forms.DateInput(format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": _("Choose a date"), "type":"date"}),


            "chronic_diseases": forms.Textarea(attrs={"class": "form-control"}),
            "permanent_medication": forms.Textarea(attrs={"class": "form-control"}),

            "publish_fotos": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }