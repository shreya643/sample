from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm


class LoginForm1(forms.Form):
   buyer_name = forms.CharField(max_length = 100)
   buyer_password = forms.CharField(widget = forms.PasswordInput())


class LoginForm2(forms.Form):
   seller_name = forms.CharField(max_length = 100)
   seller_password = forms.CharField(widget = forms.PasswordInput())


class MyRegistrationForm1(UserCreationForm):
    buyer_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
    }
    ))
    buyer_email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
    }
    ))

    class Meta:
        model = User
        fields = ('buyer_name', 'buyer_email', 'buyer_password')

    def save(self,commit = True):
        user = super(MyRegistrationForm1, self).save(commit = False)
        user.buyer_email = self.cleaned_data['buyer_email']
        user.buyer_name = self.cleaned_data['buyer_name']
        user.buyer_password = self.cleaned_data['buyer_password']

        if commit:
            user.save()

        return user


class MyRegistrationForm2(UserCreationForm):
    seller_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
    }
    ))
    seller_email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
    }
    ))

    class Meta:
        model = User
        fields = ('seller_name', 'seller_email', 'seller_password1')

    def save(self,commit = True):
        user = super(MyRegistrationForm2, self).save(commit = False)
        user.seller_email = self.cleaned_data['seller_email']
        user.seller_name = self.cleaned_data['seller_name']
        user.seller_password = self.cleaned_data['seller_password']

        if commit:
            user.save()

        return user

