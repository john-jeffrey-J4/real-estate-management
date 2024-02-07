# Generated by Django 5.0.2 on 2024-02-06 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('document_proofs', models.FileField(upload_to='tenant_documents/')),
                ('agreement_end_date', models.DateField(default=datetime.datetime(2025, 2, 5, 23, 39, 11, 52478))),
                ('monthly_rent_date', models.PositiveIntegerField(default=1)),
                ('property', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]