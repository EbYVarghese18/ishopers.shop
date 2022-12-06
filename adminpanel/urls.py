from django.urls import path
from adminpanel import views

urlpatterns = [

   
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_signin/', views.admin_signin, name='admin_signin'),
    path('admin_signout/', views.admin_signout, name='admin_signout'),

    path('admin_categories/', views.admin_categories, name='admin_categories'),
    path('admin_editcategory/<int:id>', views.admin_editcategory, name='admin_editcategory'),
    path('admin_deletecategory/<int:id>', views.admin_deletecategory, name='admin_deletecategory'),
    path('admin_addcategory/', views.admin_addcategory, name='admin_addcategory'),

    path('admin_products/', views.admin_products, name='admin_products'),
    path('admin_addproduct/', views.admin_addproduct, name='admin_addproduct'),
    # path('admin_editproduct/<int:id>', views.admin_editproduct, name='admin_editproduct'),
    # path('admin_deleteproduct/<int:id>', views.admin_deleteproduct, name='admin_deleteproduct'),
    

    # path('block_user/<int:id>/', views.block_user, name='block_user'),
    # path('unblock_user/<int:id>/', views.unblock_user, name='unblock_user'),
]