from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def all_contacts(request):
    contact_list = Employee.objects.all()
    return render(request, 'contacts.html', {'contact_list': contact_list})



