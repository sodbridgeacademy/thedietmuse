from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'category', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'category']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']

@admin.register(Specials)
class SpecialsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']