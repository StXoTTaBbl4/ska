# Generated by Django 5.0.4 on 2024-05-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_alter_certificate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateField(),
        ),
    ]