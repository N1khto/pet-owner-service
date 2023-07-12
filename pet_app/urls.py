from django.urls import path

from pet_app.views import index, SpeciesListView, SpeciesCreateView, SpeciesUpdateView, SpeciesDeleteView


urlpatterns = [
    path("", index, name="index"),
    path("species/", SpeciesListView.as_view(), name="species-list",),
    path("species/create/", SpeciesCreateView.as_view(), name="species-create",),
    path("species/<int:pk>/update/", SpeciesUpdateView.as_view(), name="species-update",),
    path("species/<int:pk>/delete/", SpeciesDeleteView.as_view(), name="species-delete",),
]

app_name = "pet_app"
