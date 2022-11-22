from django.contrib import admin
from django.urls import path

from listings.views import listing_list
from listings.views import listing_retrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<pk>/', listing_retrieve)
]
