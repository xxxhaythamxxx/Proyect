# Generated by Django 4.0.4 on 2022-11-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0161_persona_gasto_persona_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
    ]
