from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from pet_app.models import Pet, PetOwner, PetFood, Species, Brand


def index(request):

    num_pet_owners = PetOwner.objects.count()
    num_pets = Pet.objects.count()
    num_brands = Brand.objects.count()

    context = {
        "num_pet_owners": num_pet_owners,
        "num_pets": num_pets,
        "num_brands": num_brands
    }

    return render(request, "pet_app/index.html", context=context)


class SpeciesListView(LoginRequiredMixin, generic.ListView):
    model = Species
    context_object_name = "species_list"
    template_name = "pet_app/species_list.html"
    paginate_by = 2
