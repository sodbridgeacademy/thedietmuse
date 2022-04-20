from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category' 
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
    	return reverse('app:food_list_by_category', args=[self.slug])

class Food(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, related_name='categories', null=True, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='foodies/',blank=True)
    description = models.TextField(blank=True)
    return_policy = models.TextField(blank=True, null=True,)
    price = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app:food_detail', args=[self.id, self.slug])

class Event(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.CharField(max_length=500 , db_index=True)
    image = models.ImageField(upload_to='events/',blank=True)
    price = models.CharField(max_length = 50, db_index=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Specials(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(max_length=500 , db_index=True)
    image = models.ImageField(upload_to='specials/',blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='events/',blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name