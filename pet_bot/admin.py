from django.contrib import admin
from .models import Pet

admin.site.site_title = 'PetBot Admin'
admin.site.site_header = 'PetBot Admin'

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    model = Pet

admin.site.register(Pet)
