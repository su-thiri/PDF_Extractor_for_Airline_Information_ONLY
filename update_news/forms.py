from django import forms
from .models import UserImage,UserData

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['booking_code','eticket','passenger_name','travel_date','desination','departure_time','arrival_time','ar_class','baggage_allowance','flight','passport_number','price']
