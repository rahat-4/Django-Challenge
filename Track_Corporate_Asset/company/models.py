from django.db import models
from django.conf import settings
# Create your models here.

#Company detail
class Company(models.Model):
    company_name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=256)
    website = models.URLField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name



# #Asset name 
# ASSET_CHOICES = (
#     ("Phhone", "Phone"),
#     ("Laptop", "Laptop"),
#     ("Tablet", "Tablet"),
#     ("Desktop", "Desktop"),
# )

#Asset information
class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_owner = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="assets")
    asset_serial_No = models.CharField(max_length=100)
    asset_manufacturer = models.CharField(max_length=100)
    date_purchased = models.DateTimeField()
    # asset_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.asset_name

    # def get_absolute_url(self):
    #     return reverse('assets', kwargs={'pk': self.pk})


#Employee information
class Employee(models.Model):
    full_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(blank=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    company_staff = models.BooleanField(default=False)
    dob = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name


#Which employees should receive companies assets
class EmployeeAsset(models.Model):
    asset = models.ForeignKey(Asset,on_delete=models.CASCADE, related_name="employee_asset")
    asset_assigned = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="asset_taken")
    asset_returned = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.asset_assigned.full_name

#Asset condition
ASSET_CONDITIONS = (
    ('Good','Good'),
    ('Scratch','Scratch'),
    ('Broken','Broken'),
)

#Create a model for checking asset conditions and handout time before providing asset to the Employees
class AssetsCheckedOut(models.Model):
    asset_checked = models.ForeignKey(EmployeeAsset,on_delete=models.CASCADE, related_name="checked")
    is_checked_out = models.BooleanField(default=False)
    asset_checkedout_time = models.DateTimeField(auto_now_add=True)
    asset_condition = models.CharField(max_length=50, choices=ASSET_CONDITIONS, default='Good')
    
    def __str__(self):
        return self.asset_checked.asset_assigned.full_name


#Create a model for checking asset conditions and returned time after receive asset to the Employees
class AssetReturned(models.Model):
    asset_returned=models.ForeignKey(EmployeeAsset,on_delete=models.CASCADE, related_name="returned")
    is_returned = models.BooleanField(default=False)
    asset_returned_time = models.DateTimeField(blank=True, null=True)
    asset_returned_condition = models.CharField(max_length=50, choices=ASSET_CONDITIONS, default='Good')
    
    def __str__(self):
        return self.asset_returned.asset_assigned.full_name