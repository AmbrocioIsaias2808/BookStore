# Generated by Django 2.1.7 on 2019-04-19 22:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0017_auto_20190419_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='Telefono',
            field=models.IntegerField(db_column='Telefono', default=0, verbose_name='Telfono'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='FechaDePedido',
            field=models.DateField(default=datetime.datetime(2019, 4, 19, 22, 1, 7, 998970, tzinfo=utc), verbose_name='Fecha De Pedido'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Referencia',
            field=models.CharField(db_column='Referencia', default='1908040119178532', max_length=16, primary_key=True, serialize=False, verbose_name='Referencia de pago:'),
        ),
    ]
