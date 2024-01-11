from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    gender=forms.CharField(widget=forms.RadioSelect)
    password=forms.CharField(widget=forms.PasswordInput)
    phone_no=forms.IntegerField()


class CakeBookingForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    cake = forms.ChoiceField(choices=[], label='Select a Cake')
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    delivery_date = forms.DateField(label='Delivery Date')

    def _init_(self, *args, **kwargs):
        cakes = kwargs.pop('cakes', [])
        super()._init_(*args, **kwargs)
        self.fields['cake'].choices = [(cake.name, cake.name) for cake in cakes]















