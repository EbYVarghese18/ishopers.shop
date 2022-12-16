from django import forms 
from accounts.models import Account
from userprofile.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')
         