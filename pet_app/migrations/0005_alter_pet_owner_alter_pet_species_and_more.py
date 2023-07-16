# Generated by Django 4.2.3 on 2023-07-15 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pet_app", "0004_alter_pet_breed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="species",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pets",
                to="pet_app.species",
            ),
        ),
        migrations.AlterField(
            model_name="petowner",
            name="pet_owner_experience",
            field=models.PositiveIntegerField(default=0),
        ),
    ]