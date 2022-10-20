from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['day', 'name', 'slug', 'image', 'description', 'price', 'category', 'available']
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


@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_needed', 'no_of_plates', 'message', 'payment_status', 'total_cost', 'delivery_address', \
    'date_created']
    list_filter = ['date_created', 'menu', 'user']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'date_added']

@admin.register(Testimonial) 
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'image', 'testimony', 'date_added']

