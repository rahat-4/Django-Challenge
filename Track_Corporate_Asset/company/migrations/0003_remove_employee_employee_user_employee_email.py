# Generated by Django 4.1.3 on 2022-12-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_email_employee_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_user',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
