from django import forms


class SubscriptionForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")