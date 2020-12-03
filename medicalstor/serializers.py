from rest_framework import serializers
from .models import *


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializers(instance.company_id).data
        return response

class CompanyBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"
        # depth = 1

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializers(instance.company_id).data
        return response


class MedicalDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerializers(instance.medicine_id).data
        return response

class MedicalDetailserializersSimple(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"



class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializers(instance.customer_id).data
        return response




class CustomerRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = "__all__"



class EmployeeBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializers(instance.employee_id).data
        return response

class CompanyAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializers(instance.company_id).data
        return response