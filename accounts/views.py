from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView, login_required
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import UserUpdateForm, ProfileUpdateForm, FoodMenuUpdateForm
from django.contrib import messages
from app.models import FoodOrder, Food
from .models import Profile
from datetime import datetime
import time
today = datetime.today()
day = today.day
month = today.month
year = today.year

# Create your views here.
class UserRegistrationView(CreateView):
	form_class = UserCreationForm
	template_name = 'user_registration.html'

	def get_success_url(self):
		return reverse('index')


class UserLoginView(LoginView):
	 template_name = 'login.html'

@login_required
def dashboard(request):
	current_user = request.user
	print('current_user from dashboard:', current_user.first_name)
	food_menu = Food.objects.all()
	context = {'food_menu': food_menu, 'current_user':current_user}
	return render(request, 'customer_dashboard.html', context)

@login_required
def view_orders(request):
	customer_orders = FoodOrder.objects.all()
	total_customer_orders = customer_orders.count()
	init_order_cost = 0
	for p in customer_orders:
		total_costs = p.menu.price
		init_order_cost += total_costs

	total_customer_order_costs = init_order_cost

	# Pagination
	page = request.GET.get('page')
	paginator = Paginator(customer_orders, 5)
	try:
		customer_orders = paginator.page(page)
	except PageNotAnInteger:
		customer_orders = paginator.page(1) #If page is not an integer deliver the first page
	except EmptyPage:
		customer_orders = paginator.page(paginator.num_pages)

	context = {'customer_orders':customer_orders, 'total_customer_orders':total_customer_orders, \
	'total_customer_order_costs':total_customer_order_costs}
	return render(request, 'view_orders.html', context)

@login_required
def profile_update(request):
	current_user = request.user
	
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile has been updated!')
			return redirect ('dashboard')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
	'u_form':u_form,
	'p_form':p_form,
	}
	return render(request, 'user_profile.html', context)

@login_required
def food_menu(request):
	food_menu = Food.objects.all()
	context = {'food_menu': food_menu}
	return render(request, 'food_menu.html', context)

class FoodMenuUpdateView(LoginRequiredMixin, UpdateView):
	model = Food
	fields = ['name', 'category', 'image', 'day', 'description', 'price', 'available', 'return_policy']

	def form_valid(self, form):
		form.instance.user  = self.request.user
		return super().form_valid(form)

	#test function to make only an authorised user update a post
	def test_func(self):
		food_menu = self.get_object()
		if self.request.user == food_menu.user:
			return True
		return False

@login_required
def order_history(request):
	current_user = request.user	
	customer_orders = FoodOrder.objects.filter(user=current_user)
	total_customer_orders = customer_orders.count()
	order_id = int(round(time.time() * 1000))
	print(f'today= 000-{order_id}')

	# Pagination
	page = request.GET.get('page')
	paginator = Paginator(customer_orders, 4)
	try:
		customer_orders = paginator.page(page)
	except PageNotAnInteger:
		customer_orders = paginator.page(1) #If page is not an integer deliver the first page
	except EmptyPage:
		customer_orders = paginator.page(paginator.num_pages)

	init_order_cost = 0
	for p in customer_orders:
		total_costs = p.menu.price
		init_order_cost += total_costs

	total_customer_order_costs = init_order_cost
	context = {'customer_orders': customer_orders, 'total_customer_orders':total_customer_orders,\
	'total_customer_order_costs':total_customer_order_costs, 'page':page,}
	return render(request, 'order_history.html', context)


class FoodOrdersCreateView(LoginRequiredMixin, CreateView):
    model = FoodOrder
    order_id = int(round(time.time() * 1000))
    order_id = f'muse-000{order_id}'
    fields = ['menu', 'date_needed', 'no_of_plates', 'message', 'delivery_address']

    def form_valid(self, form):
        form.instance.user  = self.request.user
        form.instance.order_id = self.order_id
        return super().form_valid(form)


class FoodOrdersDetailView(DetailView):
	model = FoodOrder

class FoodMenuDetailView(DetailView):
	model = Food

class FoodOrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = FoodOrder
	fields = ['order_status', 'payment_status']
	exclude = ['user']

	def form_valid(self, form):
		self.admin = User.objects.get(username='gabby')
		print('Inside FoodOrder UpdateView:', self.admin)
		form.instance.user  = request.user
		return super().form_valid(form)

	#test function to make only an authorised user update a post
	def test_func(self):
		food_order = self.get_object()
		self.admin_user = admin
		admin = User.objects.get(username='gabby')
		if self.request.user == admin:
			return True
		return False