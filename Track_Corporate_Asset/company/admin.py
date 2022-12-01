from django.contrib import admin

from .models import Company, Employee, Asset, EmployeeAsset, AssetsCheckedOut, AssetReturned

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(EmployeeAsset)
admin.site.register(AssetsCheckedOut)
admin.site.register(AssetReturned)

