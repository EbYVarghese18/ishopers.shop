from django.urls import path
from adminpanel import views

urlpatterns = [

    path('admin_signin/', views.admin_signin, name='admin_signin'),
    path('admin_signout/', views.admin_signout, name='admin_signout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('admin_products/', views.admin_products, name='admin_products'),
    path('admin_categories/', views.admin_categories, name='admin_categories'),
    path('admin_users/', views.admin_users, name='admin_users'),

    # path('block_user/<int:id>/', views.block_user, name='block_user'),
    # path('unblock_user/<int:id>/', views.unblock_user, name='unblock_user'),
]
