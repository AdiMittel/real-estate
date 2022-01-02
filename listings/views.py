from django.shortcuts import redirect, render
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'listings':paged_listing
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')