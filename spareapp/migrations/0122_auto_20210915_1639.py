# Generated by Django 3.2.4 on 2021-09-15 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0121_rename_type_facttype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FactCategory',
        ),
        migrations.DeleteModel(
            name='factType',
        ),
        migrations.DeleteModel(
            name='factura',
        ),
        migrations.DeleteModel(
            name='persona',
        ),
    ]