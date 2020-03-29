from django import forms

class EmployeeIDForm(forms.Form):
    employeeID = forms.CharField(label='Employee ID', max_length=100)