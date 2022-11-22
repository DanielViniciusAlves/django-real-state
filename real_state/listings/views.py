from django.shortcuts import render
from .models import Listing


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