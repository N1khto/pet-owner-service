from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from pet_app.models import Pet, PetFood, Species, Brand, PetOwner


@admin.register(PetOwner)
class PetOwnerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pet_owner_experience",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("pet_owner_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("pet_owner_experience",)}),
    )


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["nickname", "age", "gender", "owner", "species", "breed"]


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["species", "animal_class", "description"]
    list_filter = ["animal_class"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(PetFood)
class PetFoodAdmin(admin.ModelAdmin):
    list_display = ["title", "brand", "food_type", "price"]
    list_filter = ["brand", "food_type"]


admin.site.unregister(Group)
