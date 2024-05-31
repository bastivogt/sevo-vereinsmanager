from members import models
from todos import models as todo_models


def do_seeds_members():
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

        email="betont.online@googlemail.com",
        phone="0176 30710872",

        publish_fotos=True,
        is_active=True,
        entry_date="2021-11-27"
    )

    member.positions.add(models.Position.objects.get(title="Vorstand"))
    member.positions.add(models.Position.objects.get(title="Trainer"))

    member.modules.add(models.Module.objects.get(title="U.C.K."))
    member.modules.add(models.Module.objects.get(title="Kickboxen"))

    member.licenses.add(models.License.objects.get(title="ÜL-C"))

    member.tariff = models.Tariff.objects.get(title="Zero")

    member.save()




    member = models.Member.objects.create(
        firstname="Ute",
        lastname="Meusel",
        birthday="1980-07-27",
        gender=models.Gender.objects.get(title="Frau"),

        street="Schillerstraße",
        house_number="33",
        postal_code="06844",
        city="Dessau-Roßlau",
        country="Deutschland",

        email="ute@meusel.de",
        phone="0176 30710872",

        publish_fotos=True,
        is_active=True,

        entry_date="2021-11-27"
    )

    member.positions.add(models.Position.objects.get(title="Vorstand"))


    member.modules.add(models.Module.objects.get(title="U.C.K."))

    member.tariff = models.Tariff.objects.get(title="Zero")

    member.save()



# members_delte_all_entries
def members_delete_all_entries():
    models.Gender.objects.all().delete()
    models.Module.objects.all().delete()
    models.Position.objects.all().delete()
    models.License.objects.all().delete()
    models.Tariff.objects.all().delete()
    models.Member.objects.all().delete()



def do_seeds_todos(request):
    todo_models.Category.objects.create(title="Allgemein")
    todo_models.Category.objects.create(title="Dachsanierung")
    
    todo = todo_models.Todo.objects.create(
        user=request.user,
        title="Herbstputz",
        content="Wir dürfen diese Jahr den Herbstputz nicht vergessen ;)"
    )

    todo.categories.add(todo_models.Category.objects.get(title="Allgemein"))
    todo.save()


    todo = todo_models.Todo.objects.create(
        user=request.user,
        title="Unterlagen KFW Bank",
        content="Restliche Unterlagen an die KFW Bank einreichen!"
    )

    todo.categories.add(todo_models.Category.objects.get(title="Dachsanierung"))
    todo.save()


# todos_delte_all_entries
def todos_delete_all_entries():
    todo_models.Category.objects.all().delete()
    todo_models.Todo.objects.all().delete()



