from django.shortcuts import render
from .models import Items
from .forms import RawProductForm

# Catalogue View
def list_view(request):
    queryset = Items.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "list.html", context)

# Input View
def input_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Items.objects.create(**form.cleaned_data)
            form = RawProductForm()
        else:
            form.errors



    context = {
        'form': form
    }
    return render(request, "input.html", context)
