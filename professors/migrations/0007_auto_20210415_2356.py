# Generated by Django 3.1.7 on 2021-04-15 15:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0006_auto_20210415_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='unique_code',
            field=models.CharField(default=uuid.uuid4, max_length=36, null=True, unique=True),
        ),
    ]
