from django.urls import path
from . import views

urlpatterns = [
    path('coupon_apply/<int:order_number>/', views.coupon_apply, name='coupon_apply'),
]
