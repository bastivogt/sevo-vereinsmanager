from django.urls import path

from members.views import members
from members.views import genders
from members.views import positions

urlpatterns = [
    # member
    path("", members.index, name="members-member-index"),


    # gender
    path("genders/", genders.index, name="members-gender-index"),
    path("gender/create", genders.create, name="members-gender-create"),
    path("gender/update/<int:id>", genders.update, name="members-gender-update"),
    path("gender/delete/<int:id>", genders.delete, name="members-gender-delete"),

    # position
    path("positions/", positions.index, name="members-position-index"),
    path("position/create", positions.create, name="members-position-create"),
    path("position/update/<int:id>", positions.update, name="members-position-update"),
    path("position/delete/<int:id>", positions.delete, name="members-position-delete"),

]