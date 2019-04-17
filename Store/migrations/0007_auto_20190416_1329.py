# Generated by Django 2.1.7 on 2019-04-16 18:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_auto_20190416_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='FechaDePedido',
            field=models.DateField(default=datetime.datetime(2019, 4, 16, 18, 29, 9, 522116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Referencia',
            field=models.CharField(db_column='Referencia', max_length=16, primary_key=True, serialize=False, verbose_name='Referencia: '),
        ),
    ]
