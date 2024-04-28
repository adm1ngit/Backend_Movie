from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)

admin.site.register(CustomUser)
admin.site.register(Actor)

class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
admin.site.register(Film, FilmAdmin)
