# Generated by Django 3.2.4 on 2021-07-11 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0093_auto_20210711_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimension',
            name='dimensionSpare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareapp.spare', verbose_name='Spare D'),
        ),
    ]
