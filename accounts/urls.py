from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    

    # email activation
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),


    # reset password
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
]
