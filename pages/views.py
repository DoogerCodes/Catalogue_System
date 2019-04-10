from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Catalogue View
def catalogue_view(request, *args, **kwargs):

    # Variable to store database items
    catalogue_listing = {
        # Entries placed here
        # list_entry = ['Deepak', '21 March 2019', True]
    }

    return render(request, "catalogue.html", catalogue_listing)

# Input View
def input_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "input.html", {})
