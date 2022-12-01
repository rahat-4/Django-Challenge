from rest_framework import generics

#create custom permissions
from .permissions import IsAdminOrReadOnly
from company.models import Company, Asset, Employee, EmployeeAsset
from .serializers import (
                          CompanySerializer, 
                          EmployeeSerializer, 
                          CompanyListSerializer,
                          EmployeeAssetSerializer,
                          AllEmployeesSerializer,
                          AssetSerializer,
                          )

#All companies list
class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    

#Individual companies details
class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'company_name'
    

#Companies assets
class CompanyAssetListView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        id = self.kwargs.get('company_id')
        assets = Asset.objects.filter(asset_owner=id)
        
        return assets
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('company_id')
        company = Company.objects.get(pk=pk)
        serializer.save(asset_owner=company)     
        

#Individual companies assets
class CompanyAssetView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        id = self.kwargs.get('pk')
        assets = Asset.objects.filter(asset_owner=company_id, id=id)
            
        return assets
    

#Individual companies all employees
class CompanyEmployeeListView(generics.ListCreateAPIView):
    serializer_class = AllEmployeesSerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        id = self.kwargs.get('company_id')
        employees = Employee.objects.filter(company_name=id)
        
        return employees
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('company_id')
        company = Company.objects.get(pk=pk)
        serializer.save(company_name=company)     
        
    

#Individual companies invidual employee information
class CompanyEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    #only superuser can handle post request otherwise it's read only
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        employee_id = self.kwargs.get('pk')
        
        employee = Employee.objects.filter(id=employee_id, company_name__id=company_id)
        
        return employee


#Given asset through companies staff
class EmployeeAssetView(generics.ListCreateAPIView):
    serializer_class = EmployeeAssetSerializer
    #only superuser can handle post request otherwise it's read only  
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        
        emp_asset = EmployeeAsset.objects.filter(asset__asset_owner=company_id, asset_assigned__company_name=company_id)
        
        return emp_asset
    