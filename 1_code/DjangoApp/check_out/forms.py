from django import forms

class NewItemsForm(forms.Form):
    new_item = forms.CharField(label='RFID', max_length=100)