from django.contrib import admin
from django import forms
from django.urls import path
from django.shortcuts import render, redirect

import csv

from .util import date_format

from .models import Customer, Order


# Register your models here.


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'date_birthday', 'date_register']
    ordering = ['first_name']

    change_list_template = "admin/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-admin-csv/', self.import_admin_csv),
        ]
        return my_urls + urls

    def import_admin_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            reader = csv.reader(chunk.decode() for chunk in csv_file)
            next(reader)
            for row in reader:
                Customer.objects.get_or_create(
                    first_name=row[0], last_name=row[1],
                    date_birthday=date_format(row[2]), date_register=date_format(row[3]))
            return redirect("..")

        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    import_admin_csv.short_description = 'Import from csv'