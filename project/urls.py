from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from medicalstor.views import *

router = routers.DefaultRouter()
router.register("company",CompanyViewSet,basename="company")
router.register("companybank",CompanyBankViewSet,basename="companybank")
router.register("medicine",MedicineViewSet,basename="medicine")
router.register("employee",EmployeeViewset,basename="employee")
router.register("customer",CustomerViewset,basename="customer")
router.register("customer-request",CustomerRequestViewset,basename="customer-request")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    # custome filter by url
    path('api/companyname/<str:name>/',CompanyNameViewSet.as_view(),name="companyname")
]
