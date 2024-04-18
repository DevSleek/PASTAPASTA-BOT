# Generated by Django 5.0.4 on 2024-04-18 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_menu_submenu_alter_submenu_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='submenu',
        ),
        migrations.AddField(
            model_name='menu',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
    ]