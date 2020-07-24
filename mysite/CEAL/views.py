from django.shortcuts import render
from django.http import HttpResponse
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max

def index(request):
    return render(request, 'CEAL/home.html')

def csv(request):
    return render(request, 'CEAL/readings.csv')



