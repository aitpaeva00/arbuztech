# Generated by Django 5.0 on 2023-12-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]