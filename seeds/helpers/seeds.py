from members import models


def do_seeds():
    # create Genders
    models.Gender.objects.create(title="Mann")
    models.Gender.objects.create(title="Frau")

    # create Positions
    models.Position.objects.create(title="Mitglied")
    models.Position.objects.create(title="Vorstand")
    models.Position.objects.create(title="Trainer")

    # create Modules
    models.Module.objects.create(title="Kung Fu")
    models.Module.objects.create(title="Kickboxen")
    models.Module.objects.create(title="U.C.K.")
    models.Module.objects.create(title="Krav Maga")
    models.Module.objects.create(title="AVCI Wing Tsun / Eskrima")

    # create Tariffs
    models.Tariff.objects.create(title="Erwachsen", amount=25)
    models.Tariff.objects.create(title="Kind", amount=20)
    models.Tariff.objects.create(title="Zero", amount=0)
    models.Tariff.objects.create(title="Eins", amount=1)

    # create Licenses
    models.License.objects.create(title="ÜL-C")

    # create Members
    gender = models.Gender.objects.get(title="Mann")

    member = models.Member.objects.create(
        firstname="Sebastian",
        lastname="Vogt",
        birthday="1981-02-27",
        gender=models.Gender.objects.get(title="Mann"),

        street="Schillerstraße",
        house_number="33",
        postal_code="06844",
        city="Dessau-Roßlau",
        country="Deutschland",

        email = "betont.online@googlemail.com",
        phone="0176 30710872",

        publish_fotos=True,
        is_active=True
    )

    member.positions.add(models.Position.objects.get(title="Vorstand"))
    member.positions.add(models.Position.objects.get(title="Trainer"))

    member.modules.add(models.Module.objects.get(title="U.C.K."))
    member.modules.add(models.Module.objects.get(title="Kickboxen"))

    member.licenses.add(models.License.objects.get(title="ÜL-C"))

    member.tariff = models.Tariff.objects.get(title="Zero")

    member.save()



def members_delete_all_entries():
    models.Gender.objects.all().delete()
    models.Module.objects.all().delete()
    models.Position.objects.all().delete()
    models.License.objects.all().delete()
    models.Tariff.objects.all().delete()
    models.Member.objects.all().delete()