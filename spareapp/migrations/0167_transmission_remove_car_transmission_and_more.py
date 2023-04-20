# Generated by Django 4.0.4 on 2023-04-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareapp', '0166_car_chasis_alter_car_transmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans', models.CharField(blank=True, max_length=20, null=True, verbose_name='Transmission')),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.ManyToManyField(blank=True, null=True, to='spareapp.transmission', verbose_name='Transmision'),
        ),
    ]