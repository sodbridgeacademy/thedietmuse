"""museproject URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserRegistrationView, UserLoginView, dashboard, FoodOrdersCreateView, FoodOrdersDetailView, \
 food_menu, order_history, profile_update, view_orders, FoodOrderUpdateView, FoodMenuUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/signup/', UserRegistrationView.as_view(), name='user-registration'),
    path('accounts/login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='logout.html',next_page=None), name = 'logout'),
    path('dashboard/',dashboard, name='dashboard'),
    path('profile-update/', profile_update, name='profile-update'),
    path('food-menu/',food_menu, name='food-menu'),
    path('food-menu/<int:pk>/update/', FoodMenuUpdateView.as_view(template_name='foodmenu_update.html'), name='menu-update'),
    path('customer-orders/',view_orders, name='view-orders'),
    path('customer/order-history/',order_history, name='order-history'),
    path('food-order/new/', FoodOrdersCreateView.as_view(template_name='foodorderform.html'), name='make-order'),
    path('customer-order/<str:pk>/confirm-payment/', FoodOrderUpdateView.as_view(template_name='customerorder_confirm.html'), name='confirm-payment'),
    path('customer-order/detail/<str:pk>/', FoodOrdersDetailView.as_view(template_name='foodorder_detail.html'), name='order-detail'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)