# Generated by Django 3.2.4 on 2021-09-27 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0135_facttype_include'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintable',
            name='tabPagos',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='tabRetiros',
        ),
        migrations.RemoveField(
            model_name='maintableaux',
            name='tabPagos',
        ),
        migrations.RemoveField(
            model_name='maintableaux',
            name='tabRetiros',
        ),
    ]