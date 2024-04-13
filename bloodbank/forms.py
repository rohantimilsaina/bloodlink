from django import forms
from .models import BloodBank, Blood, Campaign,Profile
from django.forms.widgets import DateInput


class BloodBankForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name','email','phone','number','address','facebook','insta','twitter','website']  # Ensure field names match model

class BloodBankUpdateForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['name','email','phone','number','address','facebook','insta','twitter','website','latitude','longitude']  # Ensure field names match model

class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = ['name', 'qty']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'image', 'content','date']
        
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','phone','number','address','facebook','insta','twitter','website']  # Ensure field names match model

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)