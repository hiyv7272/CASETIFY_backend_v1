# Generated by Django 3.0.1 on 2020-07-31 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_customed', models.BooleanField(null=True)),
                ('custom_info', models.TextField(max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ARTWORK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artwork.Artwork')),
                ('ARTWORK_COLOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artwork.ArtworkColor')),
                ('ARTWORK_PRICE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artwork.ArtworkPrice')),
                ('USER', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'CART',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ORDER_STATUS',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_info', models.TextField(max_length=3000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('CART', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Cart')),
                ('ORDER_STATUS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.OrderStatus')),
                ('USER', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'ORDER',
            },
        ),
    ]
