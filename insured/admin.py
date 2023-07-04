from django.contrib import admin
from .models import InsurerModel

# Register your models here.

class InsurerAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name']

admin.site.register(InsurerModel , InsurerAdmin)