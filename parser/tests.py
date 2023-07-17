import datetime

import pytest
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from .parser import ROW_START_DATA, START_DATE, add_date_column, parse_sheet


@pytest.fixture
def input_data():
    return [
        {'row_id': 1, 'company': 'company1', 'fact_qliq_data1': 10, 'fact_qliq_data2': 20, 'fact_qoil_data1': 30, 'fact_qoil_data2': 40,
            'forecast_qliq_data1': 50, 'forecast_qliq_data2': 60, 'forecast_qoil_data1': 70, 'forecast_qoil_data2': 80},
        {'row_id': 2, 'company': 'company2', 'fact_qliq_data1': 11, 'fact_qliq_data2': 21, 'fact_qoil_data1': 31, 'fact_qoil_data2': 41,
            'forecast_qliq_data1': 51, 'forecast_qliq_data2': 61, 'forecast_qoil_data1': 71, 'forecast_qoil_data2': 81},
        {'row_id': 3, 'company': 'company1', 'fact_qliq_data1': 12, 'fact_qliq_data2': 22, 'fact_qoil_data1': 32, 'fact_qoil_data2': 42,
            'forecast_qliq_data1': 52, 'forecast_qliq_data2': 62, 'forecast_qoil_data1': 72, 'forecast_qoil_data2': 82},
        {'row_id': 4, 'company': 'company2', 'fact_qliq_data1': 13, 'fact_qliq_data2': 23, 'fact_qoil_data1': 33, 'fact_qoil_data2': 43,
            'forecast_qliq_data1': 53, 'forecast_qliq_data2': 63, 'forecast_qoil_data1': 73, 'forecast_qoil_data2': 83},
    ]


def test_parse_sheet(input_data):
    sheet: Worksheet = Workbook().active
    for row in input_data:
        sheet.append(list(row.values()))
    sheet.insert_rows(0, ROW_START_DATA - 1)
    parsed_data = parse_sheet(sheet)
    assert len(input_data) == len(parsed_data)
    assert input_data == parsed_data


def test_add_date_column(input_data):
    add_date_column(input_data)
    for row in input_data:
        assert 'on_date' in row
        assert isinstance(row['on_date'], datetime.date)
        assert row['on_date'] >= START_DATE
