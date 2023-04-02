from django.urls import path
from adminpanel import views

urlpatterns = [

   
    path('admin_home/', views.admin_home, name='admin_home'),
    
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_signin/', views.admin_signin, name='admin_signin'),
    path('admin_signout/', views.admin_signout, name='admin_signout'),
    path('user_block/<int:id>/', views.user_block, name='user_block'),
    path('user_unblock/<int:id>/', views.user_unblock, name='user_unblock'),

    path('admin_categories/', views.admin_categories, name='admin_categories'),
    path('admin_addcategory/', views.admin_addcategory, name='admin_addcategory'),
    path('admin_editcategory/<int:id>', views.admin_editcategory, name='admin_editcategory'),
    path('admin_deletecategory/<int:id>', views.admin_deletecategory, name='admin_deletecategory'),
    
    path('admin_products/', views.admin_products, name='admin_products'),
    path('admin_addproduct/', views.admin_addproduct, name='admin_addproduct'),
    path('admin_editproduct/<int:id>', views.admin_editproduct, name='admin_editproduct'),
    path('admin_deleteproduct/<int:id>', views.admin_deleteproduct, name='admin_deleteproduct'),

    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('orderstatus/<int:order_number>/', views.orderstatus, name='orderstatus'),

    path('admin_coupons/', views.admin_coupons, name='admin_coupons'),
    path('add_coupon/', views.add_coupon, name='add_coupon'),
    path('edit_coupon/<int:id>/', views.edit_coupon, name='edit_coupon'),
    path('delete_coupon/<int:id>/', views.delete_coupon, name='delete_coupon'),

    path('admin_reports/', views.admin_reports, name='admin_reports'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),

]