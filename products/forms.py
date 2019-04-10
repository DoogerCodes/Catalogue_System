from django import forms

from .models import Items

class RawProductForm(forms.Form):
    Item_Description = forms.CharField(max_length=50)
    Date             = forms.DateField()
    Validity         = forms.BooleanField(required=False)
