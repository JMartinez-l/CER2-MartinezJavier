# Generated by Django 5.1.2 on 2024-10-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_pedidos_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
