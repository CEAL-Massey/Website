from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesReport
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max

#def index(request):
#    return render(request, 'CEAL/home.html')

def sales(request):
    sales =  \
    	DataPool(
           series=
            [{'options': {
                'source': SalesReport.objects.all()},
               'terms': ['month',
                'sales']},
             ])        
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False,
                  'color': '#5A7AE1'},
                'terms':{
                  'month': [
                    'sales']}}
                    ],
            chart_options =
              {'title': {
                   'text': 'Monthly Sales'},
               'xAxis': {
                   'title': {'text': 'Month'}},
                }),

    #Step 4: Send the chart object to the template.
    return render(request,'CEAL/home.html', {'cht': cht})
    
                   



