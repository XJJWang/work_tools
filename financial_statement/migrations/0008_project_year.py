# Generated by Django 5.0.6 on 2024-09-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statement', '0007_remove_project_territorial_bond_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
