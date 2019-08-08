from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.http import HttpResponse
from .models import  Branch,Bank
from .serializers import Serializer
import csv


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class Ifsc(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = Serializer(branch)
        return JsonResponse(serializer.data)

class BranchInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,city,bank):
        branch_info = Branch.objects.filter(bank__name__icontains=bank,city__iexact=city)
        serializer = Serializer(branch_info, many=True)
        return JsonResponse(serializer.data,safe=False)

def Read(request):
    # Add CSV file Path 
    csv_file = '/home/secpod/Downloads/branch.csv'
    reader = csv.DictReader(open(csv_file))
    for row in reader:
        bank_name = row.get('bank_name')
        ifsc = row.get('ifsc')
        branch = row.get('branch')
        address = row.get('address')
        city = row.get('city')
        district = row.get('district')
        state = row.get('state')
        string=''        
        if ifsc:
            bank_object, created = Bank.objects.get_or_create(name=bank_name)
            branch_info = { 'name': branch,'bank': bank_object,'address': address,'city': city,'district': district,'state': state }    
            branch_object, created = Branch.objects.update_or_create(ifsc=ifsc, defaults=branch_info)

    return HttpResponse('Done')



