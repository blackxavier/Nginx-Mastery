from django.shortcuts import render

# from django.views.decorators.vary import vary_on_headers


# @vary_on_headers("Accept-Language")
def homepage(request):
    return render(request, "new.html")
