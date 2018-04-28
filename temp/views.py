from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "temp_templates.html")


def color(request):
    return render(request, "temp/colors.html")


def tables_datatables(request):
    return render(request, "temp/tables-datatables.html")
