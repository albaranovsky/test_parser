from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from .parser import parse_sheet


def test_parse_sheet():
    data = [
        [],
        [],
        [],
        [1, 'company1', 10, 20, 30, 40, 50, 60, 70, 80],
        [2, 'company2', 11, 21, 31, 41, 51, 61, 71, 81],
        [3, 'company3', 12, 22, 32, 42, 52, 62, 72, 82],
        [4, 'company4', 13, 23, 33, 43, 53, 63, 73, 83],
    ]
    wb = Workbook()
    sheet: Worksheet = wb.active
    for row in data:
        sheet.append(row)
    parsed_data = parse_sheet(sheet)
    # for item in parsed_data:
    #     print(list(item.values()))
    assert data[3] == list(parsed_data[0].values())
