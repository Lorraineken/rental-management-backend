# Generated by Django 4.2.3 on 2023-07-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_alter_tenant_email_alter_tenant_firstname_and_more'),
        ('unit', '0003_alter_unit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='tenant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenant.tenant'),
        ),
    ]
