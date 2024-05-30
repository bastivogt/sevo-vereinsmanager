def filter(request, queryset):
    module_get = request.GET.get("module")
    position_get = request.GET.get("position")
    tariff_get = request.GET.get("tariff")
    gender_get = request.GET.get("gender")
    is_active_get = request.GET.get("is_active")
    publish_foto_get = request.GET.get("publish_foto")
    age_get = request.GET.get("age")
    order_get = request.GET.get("order")


    qs = queryset

    print(f"module: {module_get}")
    print(f"position: {position_get}")
    print(f"tariff: {tariff_get}")
    print(f"gender: {gender_get}")
    print(f"is_active: {is_active_get}")
    print(f"publish_foto: {publish_foto_get}")
    print(f"age: {age_get}")
    print(f"order: {order_get}")

    # module
    if module_get != None and module_get != "all":
        qs = qs.filter(modules__id=int(module_get))

    # position
    if position_get != None and position_get != "all":
        qs = qs.filter(positions__id=int(position_get))

    # tariff
    if tariff_get != None and tariff_get != "all":
        qs = qs.filter(tariff__id=int(tariff_get))

    # gender
    if gender_get != None and gender_get != "all":
        qs = qs.filter(gender__id=int(gender_get))

    # is_active
    if is_active_get != None and is_active_get != "all":
        is_active = True
        if is_active_get == "true":
            is_active = True
        else:
            is_active = False
        qs = qs.filter(is_active=is_active)

    # publish_foto
    if publish_foto_get != None and publish_foto_get != "all":
        publish_foto = True
        if is_active_get == "true":
            publish_foto = True
        else:
            publish_foto = False
        qs = qs.filter(publish_foto=publish_foto)


    # age
    if age_get != None and age_get != "all":
        if age_get == "lt18":
            qs = [item for item in qs if item.get_age() < 18]
        elif age_get == "gte18":
            qs = [item for item in qs if item.get_age() >= 18]
            

    # order
    if order_get != None and order_get != "none":
        if order_get == "birthday_asc":
            qs = qs.order_by("birthday")
        elif order_get == "birthday_desc":
            qs = qs.order_by("-birthday")
        elif order_get == "entry_date_asc":
            qs.order_by("entry_date")
        elif order_get == "entry_date_desc":
            qs = qs.order_by("-entry_date")
        elif order_get == "firstname_asc":
            qs = qs.order_by("firstname")
        elif order_get == "firstname_desc":
            qs = qs.order_by("-firstname")
        elif order_get == "lastname_asc":
            qs = qs.order_by("lastname")
        elif order_get == "lastname_desc":
            qs = qs.order_by("-lastname")
    
    return qs