# Generated by Django 3.2.4 on 2021-07-09 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0087_alter_reference_referencecar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atribute',
            name='atributeCategory',
        ),
        migrations.AlterField(
            model_name='atribute',
            name='atributeSpare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spareapp.spare', verbose_name='Spare'),
        ),
    ]