from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q

from members import models
from members import forms
from members.views.helper import filter

def index(request):
    members = models.Member.objects.all()
    print("tttttttttttt")
    modules = models.Module.objects.all()
    positions = models.Position.objects.all()
    licenses = models.License.objects.all()
    tariffs = models.Tariff.objects.all()
    genders = models.Gender.objects.all()


    #members
    members_data = {
        "count_all": members.count(),
        "count_active": members.filter(is_active=True).count(),
        "count_paying": members.aggregate(count=Count("tariff", filter=Q(tariff__amount__gt=0)))["count"],
        "incoming_amounts": members.aggregate(sum=Sum("tariff__amount"))["sum"],
        "age_lt_18": None,
        "age_gte_18": None
    }
    print(members_data)
    

    # modules
    modules_data = {
        "counts": {},
    }
    for module in modules:
        modules_data["counts"][module.title] = members.aggregate(count=Count("modules", filter=Q(modules__title=module.title)))["count"]
    print(modules_data)

    # positions
    positions_data = {
        "counts": {}
    }
    for position in positions:
        positions_data["counts"][position.title] = members.aggregate(count=Count("positions", filter=Q(positions__title=position.title)))["count"]
    print(positions_data)

    # licenses
    licenses_data = {
        "counts": {}
    }
    for license in licenses:
        licenses_data["counts"][license.title] = members.aggregate(count=Count("licenses", filter=Q(licenses__title=license.title)))["count"]
    print(licenses_data)

    # tariffs
    tariffs_data = {
        "counts": {},
        "sums": {},
        "sum_all" : None,
    }
    for tariff in tariffs:
        tariffs_data["counts"][tariff.title] = members.aggregate(count=Count("tariff", filter=Q(tariff__title=tariff.title)))["count"]
        tariffs_data["sums"][tariff.title] = members.aggregate(sum=Sum("tariff__amount", filter=Q(tariff__title=tariff.title)))["sum"]
        tariffs_data["sum_all"] = members.aggregate(sum=Sum("tariff__amount"))["sum"]
    print(tariffs_data)

    # genders
    genders_data = {
        "counts": {},
        "sums_amount": {}
    }
    for gender in genders:
        genders_data["counts"][gender.title] = members.aggregate(count=Count("gender", filter=Q(gender__title=gender.title)))["count"]
        genders_data["sums_amount"][gender.title] = members.aggregate(sum=Sum("tariff__amount", filter=Q(gender__title=gender.title)))["sum"]
    print(genders_data)


    # print(members.aggregate(kickboxers_count=Count("modules", modules__title="Kickboxen")))
    # print(members.annotate(test=Count("modules", modules__title="Kickboxen")))


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


    # print(members.filter(tariff__amount__gt=0))
    # print(members.aggregate(Sum("tariff__amount")))
    # print(members_paying_count)
    # print(members_paying_zero_count)
    # print(average_age)


    return render(request, "members/dashboard/index.html", {
        "title": _("Members dashboard"),
        
        "members_all_count": members_all_count,
        "members_active_count": members_active_count,
        "members_child_count": members_childs_count,
        "members_adult_count": members_adults_count,
        "members_paying_count": members_paying_count,
        "members_paying_zero_count": members_paying_zero_count,
        "incommings_all": incommings_per_month,
        "average_age": average_age,

        "items": items,
        "modules_data": modules_data


    })