from util import db_helper
from django import forms
from . import views

list = []

class SelectionForm(forms.Form):
    def __init__(self, items_list, *args, **kwargs):
        super(SelectionForm, self).__init__(*args, **kwargs)
        self.fields['selection'] = forms.ChoiceField(choices=items_list)
