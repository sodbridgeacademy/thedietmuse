from django.forms import ModelForm
from .models import FoodOrder
from django import forms
from datetimewidget.widgets import DateTimeWidget


class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(ModelForm):
	class Meta:
		Model = FoodOrder
		fields = ['menu', 'date_needed', 'no_of_plates', 'message', 'delivery_address']
		#fields = '__all__'
		exclude = ('user', 'menu',)
		widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        }
		# widgets = {
  #           'made_on': DateInput(attrs={'type': 'date'}),
  #       }
		# widgets = {
  #           'date_needed': DateInput(),
  #       }
