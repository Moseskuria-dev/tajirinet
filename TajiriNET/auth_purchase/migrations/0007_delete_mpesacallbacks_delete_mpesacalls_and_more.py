# Generated by Django 5.1.1 on 2024-10-15 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_purchase', '0006_alter_plan_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaCallBacks',
        ),
        migrations.DeleteModel(
            name='MpesaCalls',
        ),
        migrations.DeleteModel(
            name='MpesaPayment',
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={},
        ),
    ]
