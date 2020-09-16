from django.shortcuts import render
from django.http import HttpResponse
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max

def index(request):
    return render(request, 'CEAL/home.html')

def csv(request):
    return render(request, 'CEAL/readings.csv')

#def source(request):
   #return render(request, 'static/highcharts_source.js')

#def js(request):
    #return render(request, 'static/highcharts_js.js')

#def data(request):
    #return render(request, 'static/highcharts_data.js')

#def exporting(request):
    #return render(request, 'static/highcharts_exporting.js')

#def bootstrap(request):
	#return render(request, 'static/bootstrap.min.js')