# Generated by Django 5.0.6 on 2024-07-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statement', '0005_capitalflow_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitalflow',
            name='capital_type',
            field=models.CharField(choices=[('Territorial', '地方债'), ('Treasury', '国债')], max_length=50),
        ),
    ]