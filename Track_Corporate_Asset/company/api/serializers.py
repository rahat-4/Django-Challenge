from rest_framework import serializers

from company.models import Company, Employee, Asset, EmployeeAsset, AssetsCheckedOut, AssetReturned


#Companies asset details
class AssetSerializer(serializers.ModelSerializer):
    #change date format
    date_purchased = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Asset
        fields = ['id', 'asset_name', 'asset_serial_No', 'asset_manufacturer', 'date_purchased']


#Asset handout to the employees
class AssetCheckedOutSerializer(serializers.ModelSerializer):
    #change date format
    asset_checkedout_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = AssetsCheckedOut
        exclude = ['id']


#Asset return to the employees
class AssetReturnedSerializer(serializers.ModelSerializer):
    #change date format
    asset_returned_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = AssetReturned
        exclude = ['id']
        

        
#Employees received companies assets information
class EmpAssetSerializer(serializers.ModelSerializer):
    #using nested serializers
    asset = AssetSerializer(read_only=True)
    checked = AssetCheckedOutSerializer(many=True)
    returned = AssetReturnedSerializer(many=True)
    
    class Meta:
        model = EmployeeAsset
        fields = ['asset', 'checked', 'returned']

#Assigned asset to employee
class EmployeeAssetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployeeAsset
        fields = ['asset', 'asset_assigned', 'asset_returned']


#All employees information
class AllEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['company_name']


#Individual employee information
class EmployeeSerializer(serializers.ModelSerializer):
    #using nested serializer
    asset_taken = EmpAssetSerializer(many=True)
    #change date format
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Employee
        fields = ['full_name', 'designation', 'phone_number', 'dob', 'company_staff', 'date_joined', 'asset_taken']
        

#all companies list
class CompanyListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'address', 'website', 'country']

#Individual companies information
class CompanySerializer(serializers.ModelSerializer):
    #using nested serializer only for dispaly information
    assets = AssetSerializer(many=True, read_only=True)
    employees = AllEmployeesSerializer(many=True, read_only=True)
    
    class Meta:
        model = Company
        fields = ['company_name', 'address', 'website', 'country', 'assets', 'employees']
