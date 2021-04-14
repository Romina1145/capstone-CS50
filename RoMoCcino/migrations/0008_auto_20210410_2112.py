# Generated by Django 3.1.6 on 2021-04-10 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoMoCcino', '0007_auto_20210410_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='items',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoMoCcino.item'),
        ),
    ]
