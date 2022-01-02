from django.contrib import admin
from django.db.models.fields.related import RelatedField
from .models import Realtor

# Register your models here.
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

# admin.site.register(Realtor)