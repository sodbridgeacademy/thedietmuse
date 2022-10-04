from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

week_choices = (
        ('Munchy Monday', 'Munchy Monday'),
        ('Tasty Tuesday', 'Tasty Tuesday'),
        ('Wow Wednesday', 'Wow Wednesday'),
        ('Toothsome Thursday', 'Toothsome Thursday'),
        ('Fries Friday', 'Fries Friday'),
        ('Saucy Saturday', 'Saucy Saturday'),
        ('Superbowl Sunday', 'Superbowl Sunday'),
    )

order_payment_status = (
        ('Pending', 'Pending'),
        ('Received', 'Received'),
        ('Refunded', 'Refunded'),
    )

order_delivery_status = (
        ('Received', 'Received'),
        ('Incoming', 'Incoming'),
        ('Delivered', 'Delivered'),
        ('Rejected', 'Rejected'),
    )

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
    image = models.ImageField(upload_to='food-menu/',blank=True)
    day = models.CharField(max_length=20, choices=week_choices, default='Munchy Monday')
    description = models.TextField(blank=True)
    return_policy = models.TextField(blank=True, null=True,)
    price = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('day',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('food-menu')
        #return reverse('food-detail', args=[self.id, self.slug])

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


class FoodOrder(models.Model):
    menu = models.ForeignKey(Food, related_name='my_food_order', on_delete=models.CASCADE)
    date_needed = models.DateField(help_text=u'Day you need this order')
    no_of_plates = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, null=True)
    delivery_address = models.TextField(default='Ondo')
    order_status = models.CharField(max_length=50, choices=order_delivery_status, blank=True, default='Received')
    payment_status = models.CharField(max_length=50, choices=order_payment_status, blank=True, default='Pending')
    total_cost = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    order_id = models.CharField(max_length=20, blank=True, default='no order id yet')
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return str(self.menu)

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})

    def save(self):
        order_price = self.menu.price
        qnty = self.no_of_plates
        print('let us see:', order_price, qnty)
        self.total_cost = order_price * int(qnty)
        return super(FoodOrder, self).save()

class Payment(models.Model):
    food_order = models.ForeignKey(FoodOrder, related_name='which_food_order', on_delete=models.CASCADE)
    