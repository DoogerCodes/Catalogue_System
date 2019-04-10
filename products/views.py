from django.shortcuts import render
from .models import Items
from .forms import RawProductForm

# Catalogue View
def list_view(request):
    return render(request, "list.html", {})

# Input View
def input_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Items.objects.create(**form.cleaned_data)
        form = RawProductForm()

    context = {
        'form': form
    }
    return render(request, "input.html", context)
