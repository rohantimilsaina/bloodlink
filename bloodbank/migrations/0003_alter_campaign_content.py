# Generated by Django 5.0.4 on 2024-04-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "bloodbank",
            "0002_alter_blood_id_alter_bloodbank_id_alter_campaign_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="content",
            field=models.TextField(max_length=1000),
        ),
    ]
