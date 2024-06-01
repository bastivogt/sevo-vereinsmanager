import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required

from members import models

# Create your views here.

@login_required(login_url="sevo-auth-login")
def export_members(request):
    members = models.Member.objects.all().order_by("firstname")
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="members.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow([
        _("Firstname"),
        _("Lastname"),
        _("Birthday"),
        _("Gender"),

        _("Street"),
        _("House number"),
        _("Postal code"),
        _("City"),
        _("Country"),

        _("Email"),
        _("Phone"),

        _("Legal representative"),

        _("Bankname"),
        _("IBAN"),
        _("BIC"),

        _("Positions"),
        _("Modules"),
        _("Licenses"),
        _("Tariff"),
        _("Tariff amount"),
        _("Entry date"),

        _("Chronic Diseases"),
        _("Permanent medication"),

        _("Publish photos"),
        _("Is active"),

        _("Canceled at"),


    ])
    for member in members:
        writer.writerow([
            member.firstname,
            member.lastname,
            member.birthday,
            member.gender,

            member.street,
            member.house_number,
            member.postal_code,
            member.city,
            member.country,

            member.email,
            member.phone,
            
            member.legal_representative,

            member.bankname,
            member.iban,
            member.bic,

            member.get_positions_str(),
            member.get_modules_str(),
            member.get_licenses_str(),
            member.tariff.title,
            member.tariff.amount,
            member.entry_date,

            member.chronic_diseases,
            member.permanent_medication,

            member.publish_fotos,
            member.is_active,

            member.canceled_at


        ])
    return response
