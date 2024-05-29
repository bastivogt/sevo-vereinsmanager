from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

from members import models
from members import forms
from members.views.helper import filter

def index(request):
    members = models.Member.objects.all()

    members_all_count = members.count()
    members_active_count = members.filter(is_active=True).count()
    members_childs_count = len([member for member in members if member.get_age() < 18])
    members_adults_count = len([member for member in members if member.get_age() >= 18])
    members_paying_count = members.filter(tariff__amount__gt=0).count()
    members_paying_zero_count = members.filter(tariff__amount=0).count()
    incommings_per_month = members.aggregate(Sum("tariff__amount"))["tariff__amount__sum"]

    average_age = 0
    age_sum = 0
    for member in members:
        age_sum += member.get_age()

    if members.count() != 0:
        average_age = age_sum / members.count()


    items = [
        {
            "title": _("Count members"),
            "value": members_all_count
        },
        {
            "title": _("Count members active"),
            "value": members_active_count
        },
        {
            "title": _("Count members childs"),
            "value": members_childs_count
        },
        {
            "title": _("Count members adults"),
            "value": members_adults_count
        },
        {
            "title": _("Count members paying"),
            "value": members_paying_count
        },
        {
            "title": _("Count members paying zero"),
            "value": members_paying_zero_count
        },
        {
            "title": _("Incomings per month"),
            "value": incommings_per_month
        },
        {
            "title": _("Average age"),
            "value": average_age
        }
    ]


    print(members.filter(tariff__amount__gt=0))
    print(members.aggregate(Sum("tariff__amount")))
    print(members_paying_count)
    print(members_paying_zero_count)
    print(average_age)


    return render(request, "members/dashboard/index.html", {
        "title": _("Members dashboard"),
        "items": items,
        "members_all_count": members_all_count,
        "members_active_count": members_active_count,
        "members_child_count": members_childs_count,
        "members_adult_count": members_adults_count,
        "members_paying_count": members_paying_count,
        "members_paying_zero_count": members_paying_zero_count,
        "incommings_all": incommings_per_month,
        "average_age": average_age


    })