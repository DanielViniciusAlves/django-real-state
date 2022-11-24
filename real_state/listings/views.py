from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


# Using functions for simpler understanding 
def listing_list(request):
    # Return all rows in the table
    listings = Listing.objects.all()

    # Defining a dictionary
    context = {
        "listings": listings
    }

    # To return a response in Django is common to use the render
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing =  Listing.objects.get(id=pk)

    # Defining a dictionary
    context = {
        "listing": listing
    }

    # To return a response in Django is common to use the render
    return render(request, "listing.html", context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)