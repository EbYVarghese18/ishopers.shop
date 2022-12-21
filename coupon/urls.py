from django.urls import path
from coupon import views

urlpatterns = [
    path('coupon_apply/', views.coupon_apply, name='coupon_apply'),
]
