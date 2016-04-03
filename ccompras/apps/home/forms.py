from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput())
	titulo = forms.CharField(widget=forms.TextInput())
	texto = forms.CharField(widget=forms.Textarea())