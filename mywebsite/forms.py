from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100, label="Name")
    email = forms.EmailField(required=True, label="Email")
    message = forms.CharField(required=True, widget=forms.Textarea, label="Message")

    class Meta:
        model = Contact 
        fields = ('name',)