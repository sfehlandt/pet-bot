from django.contrib import admin
from .models import Pet, Task

admin.site.site_title = 'PetBot Admin'
admin.site.site_header = 'PetBot Admin'

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    model = Pet

class TaskAdmin(admin.ModelAdmin):
    model = Task
    save_as = True

admin.site.register(Pet)
admin.site.register(Task)
