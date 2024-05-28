from django.urls import path

from members.views import members
from members.views import genders
from members.views import positions
from members.views import modules
from members.views import licenses
from members.views import tariffs

urlpatterns = [
    # member
    path("members/", members.index, name="members-member-index"),
    path("member/create", members.create, name="members-member-create"),
    path("member/update/<int:id>", members.update, name="members-member-update"),
    path("member/detail/<int:id>", members.detail, name="members-member-detail"),


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

    # module
    path("modules/", modules.index, name="members-module-index"),
    path("module/create", modules.create, name="members-module-create"),
    path("module/update/<int:id>", modules.update, name="members-module-update"),
    path("module/delete/<int:id>", modules.delete, name="members-module-delete"),


    # license
    path("licenses/", licenses.index, name="members-license-index"),
    path("license/create", licenses.create, name="members-license-create"),
    path("license/update/<int:id>", licenses.update, name="members-license-update"),
    path("license/delete/<int:id>", licenses.delete, name="members-license-delete"),


    # tariff
    path("tariffs/", tariffs.index, name="members-tariff-index"),
    path("tariff/create", tariffs.create, name="members-tariff-create"),
    path("tariff/update/<int:id>", tariffs.update, name="members-tariff-update"),
    path("tariff/delete/<int:id>", tariffs.delete, name="members-tariff-delete"),

]