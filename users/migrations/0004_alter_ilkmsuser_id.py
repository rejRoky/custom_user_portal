# Generated by Django 4.1.7 on 2023-03-05 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_ilkmsuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilkmsuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]