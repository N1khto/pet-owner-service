from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class PetOwner(AbstractUser):
    pet_owner_experience = models.IntegerField()


class Species(models.Model):
    species = models.CharField(max_length=255, unique=True)
    animal_class = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)


class PetFood(models.Model):
    FOOD_TYPES = [
        ("Wet foods", "Wet foods"),
        ("Dry foods", "Dry foods"),
        ("Treat", "Treat"),
        ("Supplement", "Supplement"),
    ]

    title = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, related_name="pet_foods", on_delete=models.CASCADE)
    food_type = models.CharField(max_length=15, choices=FOOD_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


class Pet(models.Model):
    PET_GENDER = [
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    ]
    nickname = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=15, choices=PET_GENDER, null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True)
    breed = models.CharField(max_length=255)
    food = models.ManyToManyField(PetFood, related_name="pets")
