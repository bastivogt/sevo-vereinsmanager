from django.shortcuts import render
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from members import models




def redirect(request):
    url = reverse("members-member-index")
    return HttpResponseRedirect(url)


@login_required(login_url="sevo-auth-login")
def index(request):
    members = models.Member.objects.all()
    return render(request, "members/member/index.html", {
        "title": _("All members"),
        "members": members
    })