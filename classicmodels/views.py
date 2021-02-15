from django.shortcuts import render
from .models import Customers
# # Create your views here.

# def classic_homepage(request):

#     all_cust = Customers.objects.all()

#     # print(all_cust)
#     context = {'all_cust':all_cust}
#     return render(request,'classicmodels/all_cust.html',context)

from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customers

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('customernumber')
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'head','put']