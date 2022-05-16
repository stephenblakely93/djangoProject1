# Generated by Django 4.0.4 on 2022-05-15 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_remove_customer_id_customer_notes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.customer')),
                ('properties', models.CharField(max_length=200)),
                ('parameters', models.CharField(max_length=200)),
            ],
        ),
    ]
