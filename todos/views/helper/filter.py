def filter(request, queryset):

    category_get = request.GET.get("category")
    done_get = request.GET.get("done")
    order_get = request.GET.get("order")

    qs = queryset

    # categories
    if category_get != None and category_get != "all":
        qs = qs.filter(categories__id=int(category_get))

    # done
    if done_get != None and done_get != "all":
        if done_get == "true":
            qs = qs.filter(done=True)
        elif done_get == "false":
            qs = qs.filter(done=False)

    # order
    if order_get != None and order_get != "none":
        if order_get == "created_at_asc":
            qs = qs.order_by("created_at")
        elif order_get == "created_at_desc":
            qs = qs.order_by("-created_at")
        elif order_get == "updated_at_asc":
            qs = qs.order_by("updated_at")
        elif order_get == "updated_at_desc":
            qs = qs.order_by("-updated_at")

    return qs