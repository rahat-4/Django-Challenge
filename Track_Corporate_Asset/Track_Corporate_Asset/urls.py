from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #this url connect to the account apps
    path('account/', include('account.api.urls')),
    #this url connect to the company apps
    path('', include('company.api.urls')),
    
]
