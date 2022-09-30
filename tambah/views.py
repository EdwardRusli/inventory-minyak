from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from tambah.forms import Tambah_Data_Form
from tambah.models import Tambah_Data
from ambil.models import Ambil_Data
from django.db.models import Sum

def tambah(request):
    mytambahdata = Tambah_Data.objects.all().values()
    template = loader.get_template('tambah.html')
    context = {
        'mytambahdata': mytambahdata,
        'kiasstock': Tambah_Data.objects.filter(vendor='KIAS').aggregate(Sum('qtykgs')).get('qtykgs__sum') - Ambil_Data.objects.filter(lokasiambil='KIAS').aggregate(Sum('qtykgs')).get('qtykgs__sum'),
        'smartstock': Tambah_Data.objects.filter(vendor='SMART').aggregate(Sum('qtykgs')).get('qtykgs__sum') - Ambil_Data.objects.filter(lokasiambil='SMART').aggregate(Sum('qtykgs')).get('qtykgs__sum')
    }
    return HttpResponse(template.render(context, request))

def addtambah(request):
  form = Tambah_Data_Form(request.POST or None)
  if form.is_valid():
    form.save

  context = {
    'form': form
  }
  return render(request, "addtambah.html", context)

def addrecordtambah(request):
    date = request.POST['date']
    pono = request.POST['pono']
    qtykgs = request.POST['qtykgs']
    vendor = request.POST['vendor']

    tambah_data = Tambah_Data(date=date, pono=pono, qtykgs=qtykgs, vendor=vendor)
    tambah_data.save()
    return HttpResponseRedirect(reverse('tambah'))