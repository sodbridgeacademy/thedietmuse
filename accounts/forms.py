from django.contrib.auth.models import User
from .models import Profile
from app.models import FoodOrder, Food
from django import forms


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['date_created', 'subscribed_member']
		#fields = ['image', 'bank', 'bvn', 'phone_no', 'address', 'account_no', 'guarantor', 'guarantor_phone_no']

class FoodOrderUpdateForm(forms.ModelForm):
	class Meta:
		model = FoodOrder
		fields = ['menu', 'no_of_plates','delivery_address', 'order_status', 'payment_status']

class FoodMenuUpdateForm(forms.ModelForm):
	class Meta:
		model = Food
		#fields = ['menu', 'no_of_plates','delivery_address', 'user', 'order_status', 'payment_status']
		fields = '__all__'


