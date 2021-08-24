from django.http import HttpResponse
from django.contrib import admin
from .models import MatchData
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(MatchData)
class AmazonData(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]
