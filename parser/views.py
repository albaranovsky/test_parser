from django.shortcuts import redirect, render

from .models import Data
from .parser import add_date_column, open_sheet, parse_sheet


def index(request):
    err_message = ''
    if request.method == 'POST':
        try:
            sheet = open_sheet(request.FILES['xls_file'])
            data = parse_sheet(sheet)
            add_date_column(data)
            Data.objects.all().delete()
            for item in data:
                Data.objects.create(**item)
        except Exception as e:
            err_message = str(e)
        else:
            return redirect('result')

    return render(request, 'parser/index.html', {'err_message': err_message})


def result(request):
    context = {
        'data': Data.objects.all(),
        'totals': Data.totals.all()}
    return render(request, 'parser/result.html', context)
