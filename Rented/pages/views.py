from django.http import HttpRequest, HttpResponse
from django.shortcuts import render ,redirect
from . import models
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def main_page(request: HttpRequest) -> HttpResponse:
    context = {
        'listing_count': models.Listing.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'main.html', context)

def listing_list(request: HttpRequest) -> HttpResponse:
    queryset = models.Listing.objects
    context = {
        'listing_list': queryset.all(),
        'next': next,
    }
    return render(request, 'listings/listing_list.html', context)

def listing_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'listings/listing_details.html', {
        'listing': get_object_or_404(models.Listing, pk=pk)
    })

def listing_available(request: HttpRequest, pk:int) -> HttpResponse:
    listing = get_object_or_404(models.Listing, pk=pk)
    listing.is_available = not listing.is_available
    listing.save()
    messages.success(request, "{} {} {} {}".format(
        _('listing').capitalize(),
        listing.name,
        _('marked as'),
        _('available') if listing.is_available else _('unavailable'),
    ))    
    if request.GET.get('next'):
        return redirect(listing_list)
