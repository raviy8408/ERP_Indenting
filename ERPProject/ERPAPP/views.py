from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json

# Create your views here.
#
# def test(request):
#     return render(request, 'ERPAPP/Test.html')


def Table(request):
    df = pd.read_csv("/Users/Ravi/PycharmProjects/ERP_Indenting/ERPProject/ERPAPP/static/ERPAPP/csv/Test.csv")

    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'ERPAPP/Test.html', context)