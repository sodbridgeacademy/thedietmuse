from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	gender = (
			('Please select', 'Please select'),
			('Male', 'Male'),
			('Female', 'Female')
		)
	category = (
			('Choose category', 'Choose category'),
			('Monthly', 'Monthly'),
			('Quarterly', 'Quarterly'),
			('Annually', 'Annually'),
		)
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	dob = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/', default='media/default.jpeg', blank=True)
	gender = models.CharField(max_length=100, choices=gender, default='Please Select')
	category = models.CharField(max_length=100, choices=category, blank=True, default='Choose category')
	street_address = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=100, blank=True, default='Ondo')
	nationality = models.CharField(max_length=100, blank=True, default='Nigerian')
	state = models.CharField(max_length=200, blank=True, default=100)
	phone_no = models.CharField(max_length=100, blank=True)
	subscribed_member = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)