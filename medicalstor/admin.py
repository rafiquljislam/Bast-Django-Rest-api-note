from django.contrib import admin
from .models import *

admin.site.register([
        Company,
        Medicine,
        MedicalDetails,
        Employee,
        Customer,
        Bill,
        EmployeeSalary,
        BillDetails,
        CustomerRequest,
        CompanyAccount,
        CompanyBank,
        EmployeeBank,
    ])



