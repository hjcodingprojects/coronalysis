from django.shortcuts import render
import os
import pandas as pd
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def general_view(request):
    print(request.META['PATH_INFO'])
    list_url = list(
        filter(
            lambda x:bool(x),
            request.META['PATH_INFO'].split('/')
        )
    )
    if len(list_url)>1:
        countries = list_url[1:]
    else:
        countries = ['LBN']
    data_path = os.path.join(BASE_DIR, 'analyseCovid/data', 'data.csv')
    data_file = pd.read_csv(data_path, header=0, sep=';')
    list_rows = []
    for ridx, row in data_file.iterrows():
        row_dict = dict(row)
        list_rows.append(row_dict)

    data_countries = {}
    for countryItem in countries:
        values_country = list(filter(lambda itemDict: itemDict['countryterritoryCode']==countryItem, list_rows))
        values_country_sorted = sorted(values_country, key=lambda k: datetime.strptime(k['dateRep'], "%d/%m/%Y"))
        values_country_sorted_filtered = []
        for i in range(0,len(values_country_sorted)):
            if values_country_sorted[i]['cases']!=0:
                values_country_sorted_filtered = values_country_sorted[i:]
                break
        values_data_cases = list()
        values_data_death = list()
        for item in values_country_sorted_filtered:
            values_data_cases.append(item['cases'])
            values_data_death.append(item['deaths'])
        values_data_population = values_country_sorted_filtered[0]['popData2018']
        data_countries[values_country_sorted_filtered[0]['countriesAndTerritories']]=values_data_cases
    max_data = 0
    for i in data_countries.values():
        if len(i)>max_data:
            max_data = len(i)
    dict_range = {}
    print('max_data', max_data)
    dict_range['x']=list(range(1,max_data+2))
    data = dict(
        data_countries= json.dumps(data_countries),
        range_x = json.dumps(dict_range)
    )
    return render(request, 'mainAnalyse.html',data)

