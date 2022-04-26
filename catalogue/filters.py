import django_filters
from django_filters import CharFilter
from .models import *


class EmployeeFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    position = CharFilter(field_name='position', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['is_published']