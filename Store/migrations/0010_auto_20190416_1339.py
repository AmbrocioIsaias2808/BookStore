# Generated by Django 2.1.7 on 2019-04-16 18:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_auto_20190416_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='FechaDePedido',
            field=models.DateField(default=datetime.datetime(2019, 4, 16, 18, 39, 26, 353006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Referencia',
            field=models.CharField(db_column='Referencia', default='1926043916132643', max_length=16, primary_key=True, serialize=False, verbose_name='Referencia: '),
        ),
    ]
