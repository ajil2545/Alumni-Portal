from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Alumnis

def index(request):
  ouralumnis = Alumnis.objects.all().values()
  template = loader.get_template('test.html')
  context = {
    'ouralumnis': ouralumnis,
  }
  return HttpResponse(template.render(context, request))
  
def alumniReg(request):
  template = loader.get_template('alumniReg.html')
  return HttpResponse(template.render({}, request))

def addUser(request):
  x = request.POST['mail']
  y = request.POST['psw']
  a = Alumnis(email=x, password=y)
  a.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  a = Alumnis.objects.get(id=id)
  a.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  a = Alumnis.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myalumnis': a,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  mail = request.POST['mail']
  psw = request.POST['psw']
  al = Alumnis.objects.get(id=id)
  al.email = mail
  al.password = psw
  al.save()
  return HttpResponseRedirect(reverse('index'))