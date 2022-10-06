from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumniReg/', views.alumniReg, name='alumniReg'),
    path('alumniReg/addUser/', views.addUser, name='addUser'),
]