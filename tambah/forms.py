from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

vendor_choices = (
    ('KIAS', 'KIAS'),
    ('SMART', 'SMART'),
)



class Tambah_Data_Form(forms.Form):
    date = forms.DateField(widget=DateInput())
    pono = forms.CharField(max_length=255)
    qtykgs = forms.IntegerField(label='Quantity (KGs)')
    vendor = forms.ChoiceField(choices=vendor_choices)