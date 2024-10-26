# Generated by Django 5.1.2 on 2024-10-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0016_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('partialPrice', models.IntegerField()),
                ('estate', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Completado')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
    ]
