from django.urls import path, include

from .views import (
                    CompanyListView, 
                    CompanyView, 
                    CompanyEmployeeListView, 
                    CompanyEmployeeView,
                    EmployeeAssetView,
                    CompanyAssetListView,
                    CompanyAssetView,
                    )

urlpatterns = [
    #All companies name
    path('', CompanyListView.as_view(), name= "company_list"),
    #Input exact company name in url and see individual company information
    path('<company_name>/', CompanyView.as_view(), name= "company_view"),
    #Companies assets
    path('<int:company_id>/asset/', CompanyAssetListView.as_view(), name= "company_assets"),
    #Individual companies asset
    path('<int:company_id>/asset/<int:pk>', CompanyAssetView.as_view(), name= "company_assets"),
    #Individual companies all employees
    path('<int:company_id>/employee/', CompanyEmployeeListView.as_view(), name= "employee_list"),
    #Individual companies individual employee details
    path('<int:company_id>/employee/<int:pk>/', CompanyEmployeeView.as_view(), name= "employee_view"),
    #asset assigned to the employee through company
    path('<int:company_id>/asset-assign/', EmployeeAssetView.as_view(), name= "asset-assign"),
    
]

#for login
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]