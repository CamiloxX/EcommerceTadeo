# Generated by Django 5.0.2 on 2024-02-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('color Cel', 'color cel'), ('adiciones', 'adiciones'), ('firmado', 'firmado'), ('cpu', 'cpu')], max_length=100),
        ),
    ]