# Generated by Django 2.1.7 on 2019-04-16 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20190416_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='ISBN3',
            new_name='ISBN',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='ISBN2',
            new_name='ISBN',
        ),
    ]
