from django.db import models


class Data(models.Model):
    row_id = models.IntegerField()
    company = models.CharField(max_length=100)
    fact_qliq_data1 = models.IntegerField()
    fact_qliq_data2 = models.IntegerField()
    fact_qoil_data1 = models.IntegerField()
    fact_qoil_data2 = models.IntegerField()
    forecast_qliq_data1 = models.IntegerField()
    forecast_qliq_data2 = models.IntegerField()
    forecast_qoil_data1 = models.IntegerField()
    forecast_qoil_data2 = models.IntegerField()
    on_date = models.DateField()
