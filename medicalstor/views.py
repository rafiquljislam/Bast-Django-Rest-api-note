from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Company
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import TokenAuthentication


class CompanyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    authentication_classes = [TokenAuthentication, ]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializers(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Company Data save Successfully", }
        except:
            response_dict = {"error": True, "message": "Error during Saving Company Data"}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializers(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Company Data Update Successfully", }
        except:
            response_dict = {"error": True, "message": "Company Data Update False", }
        return Response(response_dict)


class CompanyBankViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]

    def create(self, request):
        try:
            serializer = CompanyBankSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "CompanyBank Data save Successfully", }
        except:
            response_dict = {"error": True, "message": "Error during Saving CompanyBank Data"}
        return Response(response_dict)

    def list(self, request):
        company = CompanyBank.objects.all()
        serializer = CompanyBankSerializers(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company CompanyBank Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializers(companybank, context={'request': request})
        return Response({'error': False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializers(companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "CompanyBank Data Update Successfully", }
        except:
            response_dict = {"error": True, "message": "CompanyBank Data Update False", }
        return Response(response_dict)


# custome filter by url
class CompanyNameViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = CompanySerializers

    def get_queryset(self):
        name = self.kwargs['name']
        return Company.objects.filter(name=name)




# MedicineSerializers
class MedicineViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]

    def create(self, request):
        try:
            serializer = MedicineSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()


            medicine_id=serializer.data['id']
            # Access The Serializer Id Which JUSt SAVE in OUR DATABASE TABLE
            # print(medicine_id)
            # Adding and Saving Id into Medicine Details Table
            medicine_details_list=[]
            for medicine_detail in request.data['medicine_details']:
                # print(medicine_detail) 
                medicine_detail['medicine_id']=medicine_id
                medicine_details_list.append(medicine_detail)
                # print(medicine_detail)
                # Adding medicine id which will work for medicine details serializer

            serializer2 = MedicalDetailserializers(data=medicine_details_list, many=True, context={"request": request})
            serializer2.is_valid()
            serializer2.save()


            response_dict = {"error": False, "message": "CompanyBank Data save Successfully", }
        except:
            response_dict = {"error": True, "message": "Error during Saving CompanyBank Data"}
        return Response(response_dict)

    def list(self, request):
        company = Medicine.objects.all()
        serializer = MedicineSerializers(company, many=True, context={"request": request})

        medicine_data = serializer.data
        newmedicinelist=[]
        # Adding Extra Key for Medicine Details in Medicine
        for medicine in medicine_data:
            # Accessing All the Medicine Details of Current Medicine ID
            medicine_details = MedicalDetails.objects.filter(medicine_id=medicine['id'])
            medicine_details_serializer = MedicalDetailserializersSimple(medicine_details,many=True)
            medicine["medicine_details"] = medicine_details_serializer.data
            newmedicinelist.append(medicine)

        response_dict = {"error": False, "message": "All Company CompanyBank Data", "data": newmedicinelist}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializers(companybank, context={'request': request})

        medicine_data = serializer.data
        # Adding Extra Key for Medicine Details in Medicine
        # Accessing All the Medicine Details of Current Medicine ID
        medicine_details = MedicalDetails.objects.filter(medicine_id=medicine_data['id'])
        medicine_details_serializer = MedicalDetailserializersSimple(medicine_details,many=True)
        medicine_data["medicine_details"] = medicine_details_serializer.data


        return Response({'error': False, "message": "Single Data Fetch", "data": medicine_data})

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializers(companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "CompanyBank Data Update Successfully", }
        except:
            response_dict = {"error": True, "message": "CompanyBank Data Update False", }
        return Response(response_dict)


class EmployeeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class CustomerViewset(viewsets.ModelViewSet):    
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerRequestViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    authentication_classes = [TokenAuthentication, ]
    queryset = CustomerRequest.objects.all()
    serializer_class = CustomerRequestSerializers