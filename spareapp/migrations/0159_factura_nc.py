# Generated by Django 3.2.4 on 2022-04-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0158_tableoperacionauxcat_tableoperacioncat'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='nc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Nota de crédito'),
        ),
    ]
