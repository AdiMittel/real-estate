from django.contrib import admin
from .models import Listing

# @admin.register(listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title',)
    list_filter = ('realtor')
    list_editable = ('is_published')
    search_field = ('title','description','address','city','state','zipcode','price')
    list_per_page = 20


admin.site.register(Listing)

# Register your models here.
