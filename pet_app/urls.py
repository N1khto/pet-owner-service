from django.urls import path

from pet_app.views import index, SpeciesListView, SpeciesCreateView, SpeciesUpdateView, \
    SpeciesDeleteView, PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView, \
    BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView, PetOwnerListView, \
    PetOwnerDetailView, PetOwnerCreateView, PetOwnerUpdateView, PetOwnerDeleteView, \
    PetFoodListView, PetFoodDetailView, PetFoodCreateView, PetFoodUpdateView, PetFoodDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("species/", SpeciesListView.as_view(), name="species-list",),
    path("species/create/", SpeciesCreateView.as_view(), name="species-create",),
    path("species/<int:pk>/update/", SpeciesUpdateView.as_view(), name="species-update",),
    path("species/<int:pk>/delete/", SpeciesDeleteView.as_view(), name="species-delete",),
    path("pets/", PetListView.as_view(), name="pet-list"),
    path("pets/<int:pk>/", PetDetailView.as_view(), name="pet-detail"),
    path("pets/create/", PetCreateView.as_view(), name="pet-create"),
    path("pets/<int:pk>/update/", PetUpdateView.as_view(), name="pet-update"),
    path("pets/<int:pk>/delete/", PetDeleteView.as_view(), name="pet-delete"),
    path("brands/", BrandListView.as_view(), name="brand-list",),
    path("brands/create/", BrandCreateView.as_view(), name="brand-create",),
    path("brands/<int:pk>/update/", BrandUpdateView.as_view(), name="brand-update",),
    path("brands/<int:pk>/delete/", BrandDeleteView.as_view(), name="brand-delete",),
    path("pet_owners/", PetOwnerListView.as_view(), name="pet-owner-list"),
    path("pet_owners/<int:pk>/", PetOwnerDetailView.as_view(), name="pet-owner-detail"),
    path("pet_owners/create/", PetOwnerCreateView.as_view(), name="pet-owner-create"),
    path("pet_owners/<int:pk>/update/", PetOwnerUpdateView.as_view(), name="pet-owner-update",),
    path("pet_owners/<int:pk>/delete/", PetOwnerDeleteView.as_view(), name="pet-owner-delete",),
    path("pet_foods/", PetFoodListView.as_view(), name="pet-food-list"),
    path("pet_foods/<int:pk>/", PetFoodDetailView.as_view(), name="pet-food-detail"),
    path("pet_foods/create/", PetFoodCreateView.as_view(), name="pet-food-create"),
    path("pet_foods/<int:pk>/update/", PetFoodUpdateView.as_view(), name="pet-food-update"),
    path("pet_foods/<int:pk>/delete/", PetFoodDeleteView.as_view(), name="pet-food-delete"),
]

app_name = "pet_app"
