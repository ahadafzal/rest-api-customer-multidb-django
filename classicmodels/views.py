from django.db.models import query
from django.shortcuts import render
from .models import Customers
# # Create your views here.

# def classic_homepage(request):

#     all_cust = Customers.objects.all()

#     # print(all_cust)
#     context = {'all_cust':all_cust}
#     return render(request,'classicmodels/all_cust.html',context)

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CustomerSerializer, EmployeeSerializer, OrderSerializer
from .models import Customers, Employees, Orders

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('customernumber')
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'head','put']

    def retrieve(self, request, *args, **kwargs):
        # ret = super(StoryViewSet, self).retrieve(request)
        custset = Customers.objects.all().filter(customernumber=kwargs['pk'])
        cust = dict(custset.values()[0])
        cust['orders_cst'] = []
        ordset =Orders.objects.all().filter(customernumber=kwargs['pk']).values()
        [cust['orders_cst'].append(dict(ord)) for ord in ordset]
        # print(cust)
        return Response(cust)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('employeenumber')
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'head','put']

   
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('ordernumber')
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'head','put']




