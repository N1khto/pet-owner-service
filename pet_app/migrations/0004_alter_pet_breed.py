# Generated by Django 4.2.3 on 2023-07-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet_app", "0003_alter_petowner_options_alter_pet_breed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="breed",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
