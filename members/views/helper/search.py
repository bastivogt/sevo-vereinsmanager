from django.db.models import Q

def search(request, queryset):
    qs = queryset

    search_get = request.GET.get("search")

    print(f"serach: {search_get}")

    if search_get != None:
        qs = qs.filter(Q(firstname__icontains=search_get) | Q(lastname__icontains=search_get))
    return qs