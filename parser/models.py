from django.db import models
from django.db.models import Sum


class TotalManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().values('on_date').annotate(
            fact_qliq_sum=(Sum('fact_qliq_data1') + Sum('fact_qliq_data2')),
            fact_qoil_sum=(Sum('fact_qoil_data1') + Sum('fact_qoil_data2')),
            forecast_qliq_sum=(
                    Sum('forecast_qliq_data1') + Sum('forecast_qliq_data2')),
            forecast_qoil_sum=(
                    Sum('forecast_qoil_data1') + Sum('forecast_qoil_data2'))
        )


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

    objects = models.Manager()
    totals = TotalManager()
