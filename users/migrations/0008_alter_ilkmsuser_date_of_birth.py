# Generated by Django 4.1.7 on 2023-03-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_ilkmsuser_birth_of_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilkmsuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth of Date'),
        ),
    ]
