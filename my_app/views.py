from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Customer
from .forms import CustomerChoiceField


def show_list(request):
    customer_choices = CustomerChoiceField()

    context = {
        'customer_choices': customer_choices,
    }

    return render(request, 'my_app/list.html', context)


def export(request):
    response = HttpResponse(content_type='text/csv')
    choice = request.GET.get('customers')

    writer = csv.writer(response)
    writer.writerow(['Customer Name', 'Properties', 'Parameters', 'Settings', 'Notes'])
    for customer in Customer.objects.filter(customer_name=choice).values_list('customer_name', 'properties',
                                                                              'parameters', 'settings', 'notes'):
        writer.writerow(customer)

    response['Content-Disposition'] = 'attachment; filename="customer_details.csv"'
    return response


def export_all(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Customer Name', 'Properties', 'Parameters', 'Settings', 'Notes'])

    for customer in Customer.objects.all().order_by('customer_name').values_list('customer_name', 'properties',
                                                                                 'parameters', 'settings',
                                                                                 'notes'):
        writer.writerow(customer)

    response['Content-Disposition'] = 'attachment; filename="all_customer_details.csv"'
    return response
