from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    # path('block_user/<int:id>/', views.block_user, name='block_user'),
    # path('unblock_user/<int:id>/', views.unblock_user, name='unblock_user'),
]
