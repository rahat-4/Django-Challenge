# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# from company.models import Employee

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
        
        

# # #to automatically create profile model
# # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# # def create_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Employee.objects.create(employee_user=instance)

# # #to automatically save on every changes of profile model
# # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# # def save_profile(sender, instance, **kwargs):
# #     instance.profile.save()