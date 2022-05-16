# Generated by Django 4.0.4 on 2022-05-15 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_remove_customerdetails_customer_notes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.customer'),
        ),
    ]