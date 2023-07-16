from django.shortcuts import redirect, render

from .models import Data
from .parser import add_date_column, open_sheet, parse_sheet


def index(request):
    if request.method == 'POST':
        sheet = open_sheet(request.FILES['xls_file'])
        data = parse_sheet(sheet)
        add_date_column(data)
        Data.objects.all().delete()
        for item in data:
            Data.objects.create(**item)

        return redirect('result')

    return render(request, 'parser/index.html')


def result(request):
    context = {'data': Data.objects.all()}
    return render(request, 'parser/result.html', context)
