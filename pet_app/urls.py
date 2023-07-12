from django.urls import path

from pet_app.views import index, SpeciesListView, SpeciesCreateView, SpeciesUpdateView, \
    SpeciesDeleteView, PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView


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
]

app_name = "pet_app"
