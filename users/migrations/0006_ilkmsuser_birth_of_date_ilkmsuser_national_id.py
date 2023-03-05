# Generated by Django 4.1.7 on 2023-03-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_ilkmsuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilkmsuser',
            name='birth_of_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Birth of Date'),
        ),
        migrations.AddField(
            model_name='ilkmsuser',
            name='national_id',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='National ID Number'),
        ),
    ]
