from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

tujuan_choices = (
    ('Ponorogo', 'Ponorogo'),
    ('Ngawi', 'Ngawi'),
    ('Caruban', 'Caruban'),
    ('Magetan', 'Magetan'),
)
lokasiambil_choices = (
    ('KIAS', 'KIAS'),
    ('SMART', 'SMART'),
)
status_choices = (
    ('On', 'On'),
    ('Off', 'Off')
)



class Ambil_Data_Form(forms.Form):
    date = forms.DateField(widget=DateInput())
    driver = forms.CharField(max_length=255)
    nopol = forms.CharField(label='Nomor Polisi', max_length=255)
    qtykgs = forms.IntegerField(label='Quantity (KGs)')
    tujuan = forms.ChoiceField(choices=tujuan_choices)
    lokasiambil = forms.ChoiceField(label='Lokasi Ambil', choices=lokasiambil_choices)
    status = forms.ChoiceField(choices=status_choices)

class Ambil_Data_Edit_Form(forms.Form):
    date = forms.DateField(widget=DateInput())
    dono = forms.CharField(label='DO No', max_length=255)
    driver = forms.CharField(max_length=255)
    nopol = forms.CharField(label='Nomor Polisi', max_length=255)
    qtykgs = forms.IntegerField(label='Quantity (KGs)')
    tujuan = forms.ChoiceField(choices=tujuan_choices)
    lokasiambil = forms.ChoiceField(label='Lokasi Ambil', choices=lokasiambil_choices)
    status = forms.ChoiceField(choices=status_choices)

    # class Meta:
    #     model = Ambil_Data
    #     fields = [
    #         "date",
    #         "dono",
    #         "driver",
    #         "nopol",
    #         "qtykgs",
    #         "tujuan",
    #         "lokasiambil",
    #         "status",
    #     ]