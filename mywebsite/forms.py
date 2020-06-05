from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, label="Name")
    email = forms.EmailField(required=True, label="Email")
    message = forms.CharField(required=True, widget=forms.Textarea)