# Generated by Django 2.1.7 on 2019-04-16 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_auto_20190416_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='FechaDePedido',
            field=models.DateField(default=datetime.datetime(2019, 4, 16, 18, 31, 29, 127527, tzinfo=utc)),
        ),
    ]
