# Generated by Django 5.0.6 on 2024-09-19 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statement', '0008_project_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitalflow',
            old_name='account',
            new_name='amount',
        ),
    ]
