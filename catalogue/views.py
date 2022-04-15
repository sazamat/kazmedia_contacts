from django.db.transaction import commit
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q


def all_contacts(request):
    if 'q' in request.GET:
        q = request.GET["q"]
        # contact_list = Employee.objects.filter(name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(cell__icontains=q) | Q(position__icontains=q))
        contact_list = Employee.objects.filter(multiple_q)
    else:
        contact_list = Employee.objects.all()

    return render(request, 'contacts.html', {'contact_list': contact_list})
