from django import forms

from .models import Items

class RawProductForm(forms.Form):
    Item_Description = forms.CharField(max_length=50, label='Item Name', widget=forms.TextInput(attrs={"placeholder": "Ex: Laptop"}))
    Date             = forms.DateField(label='Date',
                    widget=forms.TextInput(attrs={"placeholder": "Ex: 2019-01-01"}))
    Validity         = forms.BooleanField(required=False)

# class Meta:
#     model = Items
#     fields = [
#
#     ]
#
# def clean_date(self, *args, **kwargs):
#     Date =
