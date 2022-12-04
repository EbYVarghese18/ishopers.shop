from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('admin_signin/', views.admin_signin, name='admin_signin'),
    path('admin_signout/', views.admin_signout, name='admin_signout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('admin_products/', views.admin_products, name='admin_products'),
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_categories/', views.admin_categories, name='admin_categories'),

]
