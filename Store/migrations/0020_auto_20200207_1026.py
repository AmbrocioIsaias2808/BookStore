# Generated by Django 3.0.3 on 2020-02-07 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0019_auto_20190421_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='FechaDePedido',
            field=models.DateField(default=datetime.datetime(2020, 2, 7, 16, 26, 54, 520091, tzinfo=utc), verbose_name='Fecha De Pedido'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Referencia',
            field=models.CharField(db_column='Referencia', default='2054022607108397', max_length=16, primary_key=True, serialize=False, verbose_name='Referencia de pago:'),
        ),
    ]
