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