from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView, login_required
from app.models import FoodOrder, Food

# Create your views here.
class UserRegistrationView(CreateView):
	form_class = UserCreationForm
	template_name = 'user_registration.html'

	def get_success_url(self):
		return reverse('index')


class UserLoginView(LoginView):
	 template_name = 'user_login.html'

@login_required
def dashboard(request):
	food_menu = Food.objects.all()
	context = {'food_menu': food_menu}
	return render(request, 'dashboard.html', context)

@login_required
def food_menu(request):
	food_menu = Food.objects.all()
	context = {'food_menu': food_menu}
	return render(request, 'food_menu.html', context)

@login_required
def order_history(request):
	current_user = request.user
	customer_orders = FoodOrder.objects.filter(user=current_user)
	total_customer_orders = customer_orders.count()
	context = {'customer_orders': customer_orders, 'total_customer_orders':total_customer_orders}
	return render(request, 'order_history.html', context)


class FoodOrdersCreateView(LoginRequiredMixin, CreateView):
    model = FoodOrder
    fields = ['menu', 'date_needed', 'no_of_plates', 'message', 'delivery_address']

    def form_valid(self, form):
        form.instance.user  = self.request.user
        return super().form_valid(form)