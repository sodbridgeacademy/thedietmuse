"""museproject URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserRegistrationView, UserLoginView, dashboard, FoodOrdersCreateView, FoodOrdersDetailView, password_reset_request, \
    food_menu, order_history, profile_update, view_orders, FoodOrderUpdateView, FoodMenuUpdateView, FoodMenuDetailView, FoodMenuDeleteView
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    # sign up/in urls
    path('accounts/signup/', UserRegistrationView.as_view(), name='user-registration'),
    path('accounts/login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='app/index.html',next_page=None), name = 'logout'),

    # user prodile urls
    path('user-profile/',dashboard, name='dashboard'),
    path('user-profile-update/', profile_update, name='profile-update'),

    # food menu/order urls
    path('food-menu/',food_menu, name='food-menu'),
    path('food-menu/<int:pk>/update/', FoodMenuUpdateView.as_view(template_name='foodmenu_update.html'), name='menu-update'),
    path('food-menu/<int:pk>/detail/', FoodMenuDetailView.as_view(template_name='foodmenu_detail.html'), name='menu-detail'),
    path('food-menu/<int:pk>/delete/', FoodMenuDeleteView.as_view(template_name='foodmenudelete_form.html'), name='menu-delete'),
    path('customer-orders/',view_orders, name='view-orders'),
    path('customer/order-history/',order_history, name='order-history'),
    path('food-order/new/', FoodOrdersCreateView.as_view(template_name='foodorderform.html'), name='make-order'),
    path('customer-order/<str:pk>/confirm-payment/', FoodOrderUpdateView.as_view(template_name='customerorder_confirm.html'), name='confirm-payment'),
    path('customer-order/detail/<str:pk>/', FoodOrdersDetailView.as_view(template_name='foodorder_detail.html'), name='order-detail'),

    # change password urls
    path('password_change/', PasswordChangeView.as_view(template_name='password_change_form.html'),name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    # reset password urls
    path('password_reset/', PasswordResetView.as_view(template_name='password/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),name='password_reset_complete'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)