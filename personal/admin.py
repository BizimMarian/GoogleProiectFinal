from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Horror, Comedie, Actiune,Drama)
class ViewAdmin(admin.ModelAdmin):
    pass
