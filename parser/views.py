from django.shortcuts import redirect, render

from .models import Data
from .parser import add_date_column, open_sheet, parse_sheet


def index(request):
    err_message = ''
    bulk_list = []
    if request.method == 'POST':
        Data.objects.all().delete()
        try:
            sheet = open_sheet(request.FILES['xls_file'])
            rows = parse_sheet(sheet)
            add_date_column(rows)
            for row in rows:
                bulk_list.append(Data(**row))
            Data.objects.bulk_create(bulk_list)
        except Exception as e:
            err_message = str(e)
        else:
            return redirect('result')

    return render(request, 'parser/index.html', {
        'err_message': err_message
    })


def result(request):
    return render(request, 'parser/result.html', {
        'rows': Data.objects.all(),
        'totals': Data.totals.all()
    })
