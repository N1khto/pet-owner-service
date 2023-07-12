from django.urls import path

from pet_app.views import index, SpeciesListView


urlpatterns = [
    path("", index, name="index"),
    path("species/", SpeciesListView.as_view(), name="species-list",)
]


app_name = "pet_app"
