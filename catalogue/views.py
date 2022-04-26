from django.db.transaction import commit
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .filters import EmployeeFilter


def all_contacts(request):
    contact_list = Employee.objects.all()
    myFilter = EmployeeFilter(request.GET, queryset=contact_list)
    contact_list = myFilter.qs
    return render(request, 'contacts.html', {'contact_list': contact_list, 'myFilter': myFilter})


def home(request):
    return render(request, 'home.html')
