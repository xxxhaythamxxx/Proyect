# Generated by Django 3.2.4 on 2021-06-21 19:42

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0040_auto_20210621_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='referenceSpare',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='referenceCategory', chained_model_field='spare_category', null=True, on_delete=django.db.models.deletion.CASCADE, to='spareapp.spare', verbose_name='Spare'),
        ),
    ]