# Generated by Django 5.0.6 on 2024-07-04 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0005_filebook_bookshelf_alter_filebook_cell'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filebook',
            name='bookshelf',
        ),
    ]
