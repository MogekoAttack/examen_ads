# Generated by Django 4.2.6 on 2023-10-22 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo', '0001_initial'),
        ('shopping_car', '0001_initial'),
        ('store_customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcar',
            name='assigned_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='store_customer.userstore', verbose_name='Usuario asignado'),
        ),
        migrations.AddField(
            model_name='sale',
            name='assigned_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.book', verbose_name='Libro a comprar'),
        ),
        migrations.AddField(
            model_name='sale',
            name='assigned_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_car.shoppingcar', verbose_name='Carrito asociado'),
        ),
        migrations.AddField(
            model_name='sale',
            name='assigned_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_customer.userstore', verbose_name='Usuario asignado a carrito'),
        ),
    ]
