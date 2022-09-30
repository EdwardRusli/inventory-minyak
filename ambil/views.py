from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Ambil_Data
from .forms import Ambil_Data_Form, Ambil_Data_Edit_Form
from tambah.models import Tambah_Data
from django.db.models import Sum
from datetime import datetime

def ambil(request):
  myambildata = Ambil_Data.objects.all().values()
  template = loader.get_template('ambil.html')
  context = {
    'myambildata': myambildata,
    # 'kiasstock': Tambah_Data.objects.filter(vendor='KIAS').aggregate(Sum('qtykgs')).get('qtykgs__sum') - Ambil_Data.objects.filter(lokasiambil='KIAS').aggregate(Sum('qtykgs')).get('qtykgs__sum'),
    # 'smartstock': Tambah_Data.objects.filter(vendor='SMART').aggregate(Sum('qtykgs')).get('qtykgs__sum') - Ambil_Data.objects.filter(lokasiambil='SMART').aggregate(Sum('qtykgs')).get('qtykgs__sum')
       'kiasstock': 0,
       'smartstock': 0
  }
  return HttpResponse(template.render(context, request))

# def add(request):
#   template = loader.get_template('add.html')
#   return HttpResponse(template.render({}, request))

def addambil(request):
  form = Ambil_Data_Form(request.POST or None)
  if form.is_valid():
    form.save

  context = {
    'form': form
  }
  return render(request, "addambil.html", context)

def addrecordambil(request):
  date = request.POST['date']
  driver = request.POST['driver']
  nopol = request.POST['nopol']
  qtykgs = request.POST['qtykgs']
  tujuan = request.POST['tujuan']
  lokasiambil = request.POST['lokasiambil']
  status = request.POST['status']

  dateparsed = datetime.strptime(date, "%Y-%m-%d")
  doindex = 1
  dono = f'SJ/{"{:02d}".format(doindex)}/{dateparsed.strftime("%m")}{dateparsed.strftime("%y")}'
  while(Ambil_Data.objects.filter(dono=dono).exists()):
    doindex += 1
    dono = f'SJ/{"{:02d}".format(doindex)}/{dateparsed.strftime("%m")}{dateparsed.strftime("%y")}'
  
  ambil_data = Ambil_Data(date = date, dono = dono, driver = driver, nopol = nopol, qtykgs = qtykgs, tujuan = tujuan, lokasiambil = lokasiambil, status = status)
  ambil_data.save()


  return HttpResponseRedirect(reverse('ambil'))

def deleteambil(request, id):
  data_ambil = Ambil_Data.objects.get(id=id)
  data_ambil.delete()
  return HttpResponseRedirect(reverse('ambil'))

# def update(request, id):
#   myambildata = Ambil_Data.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'myambildata' : myambildata,
#   }
#   return HttpResponse(template.render(context, request))
def updateambil(request, id):  
  myambildata = Ambil_Data.objects.get(id=id)

  form = Ambil_Data_Edit_Form(request.POST or None)
  if form.is_valid():
    form.save

  context = {
    'form': form,
    'myambildata' : myambildata,
  }
  return render(request, "updateambil.html", context)

def updaterecordambil(request, id):
  date = request.POST['date']
  dono = request.POST['dono']
  driver = request.POST['driver']
  nopol = request.POST['nopol']
  qtykgs = request.POST['qtykgs']
  tujuan = request.POST['tujuan']
  lokasiambil = request.POST['lokasiambil']
  status = request.POST['status']

  ambil_data = Ambil_Data.objects.get(id=id)
  ambil_data.date = date
  ambil_data.dono = dono
  ambil_data.driver = driver
  ambil_data.nopol = nopol
  ambil_data.qtykgs = qtykgs
  ambil_data.tujuan = tujuan
  ambil_data.lokasiambil = lokasiambil
  ambil_data.status = status
  ambil_data.save()
  return HttpResponseRedirect(reverse('ambil'))